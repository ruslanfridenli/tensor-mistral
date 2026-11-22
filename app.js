const I18N={"en":{"controls":"Controls","params":"Parameters","corpus":"Corpus","length":"Length","temp":"Creativity","gen":"✦ Generate","words":"Words","placeholder":"press generate — a python markov chain writes for you"},"de":{"controls":"Steuerung","params":"Parameter","corpus":"Korpus","length":"Länge","temp":"Kreativität","gen":"✦ Generieren","words":"Wörter","placeholder":"generieren drücken — eine python-markov-kette schreibt für dich"}};
let lang=localStorage.getItem('lang')||'en';
const t=k=>I18N[lang][k]||k;
function applyLang(){document.documentElement.lang=lang;document.querySelectorAll('[data-i]').forEach(el=>el.textContent=t(el.dataset.i));document.querySelectorAll('.lang button').forEach(b=>b.classList.toggle('on',b.dataset.lang===lang));}
document.querySelectorAll('.lang button').forEach(b=>b.onclick=()=>{lang=b.dataset.lang;localStorage.setItem('lang',lang);applyLang();});

const $=id=>document.getElementById(id);let py=null;
async function boot(){py=await loadPyodide();py.runPython(await(await fetch('app.py')).text());}
$('gen').onclick=()=>{
  const corpus=$('corpus').value,len=+$('length').value,temp=+$('temp').value;
  const text=py.globals.get('gen_text')(corpus,len,temp);
  const out=$('out');out.innerHTML='';const p=document.createElement('p');p.textContent=text;out.appendChild(p);
  $('wc').textContent=text.split(/\s+/).filter(Boolean).length;
};
boot().catch(e=>console.error(e));applyLang();