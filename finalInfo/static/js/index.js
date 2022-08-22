const menu = document.querySelector(".btn-menu")
const navbar = document.querySelector(".nav-search")

menu.addEventListener("click",()=>{
   navbar.style["display"] == "flex" ? navbar.style["display"] = "none" : navbar.style["display"] = "flex"
})