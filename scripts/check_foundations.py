"""Independent numerical checks for Chapters 1--6 (Python + NumPy).
Run from any directory. Assertions test physical invariants, independent
quantum/classical propagation, Fourier quadrature and analytic covariance.
"""
from pathlib import Path
import re
import numpy as np
from numpy.testing import assert_allclose as close

ROOT = Path(__file__).resolve().parents[1]
integrate = getattr(np, "trapezoid", None) or np.trapz
rng = np.random.default_rng(1046)
checks = 0
def check(a, b, **kw):
    global checks
    close(a, b, rtol=kw.get("rtol", 1e-10), atol=kw.get("atol", 1e-11))
    checks += 1

sx = np.array([[0,1],[1,0]], complex)
sy = np.array([[0,-1j],[1j,0]])
sz = np.diag([1.,-1.])
pauli = np.array([sx,sy,sz])
eye = np.eye(2)
def rotation(p, n, angle):
    n = np.asarray(n, float)/np.linalg.norm(n)
    return p*np.cos(angle)+np.cross(n,p)*np.sin(angle)+n*np.dot(n,p)*(1-np.cos(angle))

# Quantum unitary against independently constructed Rodrigues rotations.
for _ in range(40):
    p = rng.normal(size=3); p /= 1+np.linalg.norm(p)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    alpha = rng.uniform(-8,8)
    rho = (eye+np.einsum('i,ijk->jk',p,pauli))/2
    U = np.cos(alpha/2)*eye+1j*np.sin(alpha/2)*np.einsum('i,ijk->jk',n,pauli)
    out = U@rho@U.conj().T
    pq = np.array([np.trace(out@s).real for s in pauli])
    check(pq, rotation(p,n,-alpha))
    check(np.linalg.eigvalsh(out),np.linalg.eigvalsh(rho))
check(rotation(np.array([0.,0,1]),[1,0,0],-np.pi/2),[0,1,0])

# General-phase pi conjugation and static-offset echo.
for phi in [.0,.3,1.7]:
    p = np.array([.2,.7,-.1])
    out = rotation(p,[np.cos(phi),np.sin(phi),0],-np.pi)
    check(out[0]+1j*out[1], np.exp(2j*phi)*(p[0]-1j*p[1]))
    for delta in [-813,0,1709]:
        tau=.027
        free=rotation(p,[0,0,1],-delta*tau)
        pulse=rotation(free,[np.cos(phi),np.sin(phi),0],-np.pi)
        echo=rotation(pulse,[0,0,1],-delta*tau)
        check(echo[0]+1j*echo[1],np.exp(2j*phi)*(p[0]-1j*p[1]))

# RK4 integrates the Cartesian differential equation independently of closed forms.
def rk4(rhs,y,t,steps):
    h=t/steps; y=np.array(y,float)
    for j in range(steps):
        u=j*h
        a=rhs(u,y); b=rhs(u+h/2,y+h*a/2)
        c=rhs(u+h/2,y+h*b/2); d=rhs(u+h,y+h*c)
        y += h*(a+2*b+2*c+d)/6
    return y
w1=500*np.pi; delta=1000*np.pi; T=.001
out=rk4(lambda t,m:np.cross(m,[w1,0,delta]),[0,0,1],T,800)
O=np.hypot(w1,delta)
analytic=[w1*delta/O**2*(1-np.cos(O*T)),w1/O*np.sin(O*T),
          (delta**2+w1*w1*np.cos(O*T))/O**2]
check(out,analytic)
print("Detuned 90-degree pulse:",np.round(out,6))
A=np.array([[-10,100,0],[-100,-10,10],[0,-10,-1.]])
b=np.array([0,0,1.])
check(np.linalg.solve(-A,b),[10/111,1/111,101/111])
out=rk4(lambda t,m:np.array([-m[0]/.08,-m[1]/.08,(1-m[2])/1.2]),
         [.7,.2,-.9],.6,1000)
check(out,[.7*np.exp(-.6/.08),.2*np.exp(-.6/.08),1-1.9*np.exp(-.5)])

# Small-tip formula checked by time quadrature and weak-drive Bloch integration.
T=.012; d=137.; w=.06/T
tt=np.linspace(0,T,12001)
drive=w*np.sin(np.pi*tt/T)**2
sta=1j*integrate(drive*np.exp(-1j*d*(T-tt)),tt)
bloch=rk4(lambda t,m:np.cross(m,[w*np.sin(np.pi*t/T)**2,0,d]),[0,0,1],T,2400)
check(bloch[0]+1j*bloch[1],sta,rtol=2e-4)
# Biphasic closed-form sign, using separate half integrals.
T=.01; d=67.; w=.4
tt=np.linspace(0,T/2,10001)
quad=1j*w*(integrate(np.exp(-1j*d*(T-tt)),tt)-
           integrate(np.exp(-1j*d*(T-(tt+T/2))),tt))
check(quad,-w/d*(1-np.exp(-1j*d*T/2))**2,rtol=1e-9)

# Continuous Fourier Gaussian, voxel integral, and finite DFT inversion.
x=np.linspace(-9,9,100001)
for k in [0,.2,.7]:
    check(integrate(np.exp(-x*x/2)*np.exp(-2j*np.pi*k*x),x),
          np.sqrt(2*np.pi)*np.exp(-2*np.pi**2*k*k))
x=np.linspace(-.5,.5,100001)
check(integrate(np.exp(-2j*np.pi*.5*x),x),2/np.pi,rtol=1e-9)
N=16; j=np.arange(N)
F=np.exp(-2j*np.pi*np.outer(j,j)/N)
check(F.conj().T@F,N*np.eye(N))
v=rng.normal(size=N)+1j*rng.normal(size=N)
check(F.conj().T@(F@v)/N,v)
sig=8.
check(F.conj().T@(2*sig**2*np.eye(N))@F/N**2,2*sig**2/N*np.eye(N))
w=(1-np.cos(2*np.pi*j/N))/2
C=F.conj().T@np.diag(w*w)@F/N**2
pred=np.zeros((N,N))
for m in j:
    for n in j:
        d=(m-n)%N
        pred[m,n]=({0:3/8,1:-1/4,N-1:-1/4,2:1/16,N-2:1/16}.get(d,0))/N
check(C,pred)

# Fisher information: analytic Schur complement against derivative columns.
A0=100; tau=.08; t=.087
J=np.array([[1,0],[np.exp(-t/tau),A0*t/tau**2*np.exp(-t/tau)]])
I=J.T@J
check(I[1,1]-I[1,0]**2/I[0,0],A0**2*t*t/(tau**4*(np.exp(2*t/tau)+1)))
u=1.
for _ in range(30): u=1+np.exp(-2*u)
check(u,1.1088575528785,atol=1e-10)
for rho in [0,.5,-.6]:
    psi=np.array([[1,rho],[rho,1.]])
    a=np.array([1,2.])
    w=np.linalg.solve(psi,a); w/=a@w
    check(w,np.array([1-2*rho,2-rho])/(5-4*rho))
    check(w@psi@w,(1-rho*rho)/(5-4*rho))

# Numerical values, using the book's rounded gamma.
gb=42.57748e6; gamma=2*np.pi*gb; hbar=1.054571817e-34; kb=1.380649e-23
pol=np.tanh(hbar*gamma*3/(2*kb*310))
M0=6.69e28*gamma*hbar/2*pol
print(f"3 T: f={gb*3/1e6:.8f} MHz; p={pol:.9g}; M0={M0:.9g} A/m")
print(f"Readout example: G={1/(.24*gb*4e-6)*1e3:.6f} mT/m; area={256/(2*.24*gb)*1e6:.6f} uT s/m")
area=500/gb
print(f"Problem 5.1: G={1/(.256*gb*5e-6)*1e3:.6f} mT/m; area={area*1e6:.6f}; Tmin={(area/.04+.04/150)*1e3:.6f} ms")
check(np.exp(-.02/.08-(2*np.pi*20*.02)**2/2),.0331,rtol=.002)
check(pol,9.8874e-6,rtol=1e-6)

# Dimensional algebra with independent base exponents: (mass,length,time,current).
def add(*args): return tuple(sum(v) for v in zip(*args))
def mul(a,n): return tuple(n*v for v in a)
B=(1,0,-2,-1); length=(0,1,0,0); time=(0,0,1,0); current=(0,0,0,1)
gyr=add(mul(B,-1),mul(time,-1)); grad=add(B,mul(length,-1))
check(add(gyr,grad,length,time),(0,0,0,0))
check(add(gyr,grad,time),(0,-1,0,0))
moment=add(current,mul(length,2)); energy=(1,2,-2,0)
check(add(moment,B),energy)
mag=add(current,mul(length,-1))
coil=add(B,mul(current,-1))
flux=add(coil,mag,mul(length,3))
check(flux,(1,2,-2,-1))
for order in range(3):
    gm=add(grad,mul(time,order+1))
    velocity_order=add(length,mul(time,-order))
    check(add(gyr,gm,velocity_order),(0,0,0,0))

# Foundation-specific coverage and absence of empty leaf sections.
chapters=sorted((ROOT/'chapters').glob('*.tex'))[:6]
problems=[]
figures=[]
for path in chapters:
    s=path.read_text(encoding='utf-8-sig')
    clean=re.sub(r'(?m)(?<!\\)%.*$','',s)
    assert not re.search(r'\b(TODO|TBD|placeholder|lorem ipsum)\b',clean,re.I),path
    leaves=re.split(r'\\subsection\{[^}]*\}',clean)[1:]
    for leaf in leaves:
        body=re.split(r'\\(?:subsection|section)\{',leaf)[0]
        assert len(re.findall(r'[A-Za-z]{2,}',body))>=20,(path,body[:90])
    pp=re.findall(r'\\label\{(prob:[^}]+)\}',s)
    assert len(pp)==5,(path,len(pp))
    problems+=pp
    figures+=re.findall(r'\\input\{(figures/[^}]+)\}',s)
sol=(ROOT/'appendices/E_solutions.tex').read_text(encoding='utf-8-sig')
targets=re.findall(r'\\begin\{solution\}\{([^}]+)\}',sol)
assert sorted(targets)==sorted(problems)
assert len(figures)==7
assert all((ROOT/(f+'.tex')).exists() for f in figures)
print(f"PASS: {checks} numerical/dimensional assertions; 30 matched solutions; 7 vector figures; no empty foundational subsections.")
