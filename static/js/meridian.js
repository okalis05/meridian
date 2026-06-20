// Small polished interaction layer.
document.querySelectorAll('.card').forEach(card=>{card.addEventListener('mousemove',e=>{card.style.transform='translateY(-3px)';});card.addEventListener('mouseleave',()=>{card.style.transform='';});});
