(function(){
var d=document,w=window;
if(!('IntersectionObserver' in w))return;
if(w.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var root=d.querySelector('#bsx-proofbar');
if(!root)return;
var vh=w.innerHeight;
var stags=[].slice.call(d.querySelectorAll('.bsx-sec .bsx-stag'));
var later=stags.filter(function(el){return el.getBoundingClientRect().top>vh*0.9;});
later.forEach(function(el){el.classList.remove('bsx-in');});
d.body.classList.add('bsx-armed');
function count(el){
  var to=parseFloat(el.getAttribute('data-pbto')),from=parseFloat(el.getAttribute('data-pbfrom')||'0');
  var dec=parseInt(el.getAttribute('data-pbdec')||'0',10),pre=el.getAttribute('data-pbpre')||'',suf=el.getAttribute('data-pbsuf')||'';
  var t0=null,dur=1100;
  function step(ts){if(t0===null){t0=ts;}var p=Math.min(1,(ts-t0)/dur);var e=1-Math.pow(1-p,3);
    el.textContent=pre+(from+(to-from)*e).toFixed(dec)+suf;if(p<1){w.requestAnimationFrame(step);}}
  w.requestAnimationFrame(step);
}
var io=new IntersectionObserver(function(ents){
  ents.forEach(function(en){
    if(!en.isIntersecting)return;
    var el=en.target;el.classList.add('bsx-in');io.unobserve(el);
    if(el.classList.contains('bsx-pbgrid')){[].forEach.call(el.querySelectorAll('[data-pbto]'),count);}
  });
},{rootMargin:'0px 0px -8% 0px',threshold:0.08});
later.forEach(function(el){io.observe(el);});
})();
