const input=document.getElementById("password");
const toggle=document.getElementById("toggle");
toggle?.addEventListener("click",()=>{
  const visible=input.type==="text";
  input.type=visible?"password":"text";
  toggle.textContent=visible?"SHOW":"HIDE";
  toggle.setAttribute("aria-label",visible?"Show password":"Hide password");
});
document.querySelectorAll("[data-example]").forEach(button=>{
  button.addEventListener("click",()=>{
    input.value=button.dataset.example;
    input.focus();
  });
});
// Educational demo only: no password storage, analytics, or console logging.
