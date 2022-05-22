const Open_calculator = document.getElementById("open_calculator");
const Close_calculator = document.querySelector(".close_calculator");
const Calculator = document.querySelector(".calculator");

Open_calculator.addEventListener("click", () =>{
    Calculator.style.display = "block";
});

Close_calculator.addEventListener("click", () =>{
    Calculator.style.display = "none";
});

document.addEventListener("click", (e) =>{
    if (e.target == Calculator){
        Calculator.style.display = "none";
    }
});

const Open_notepad = document.getElementById("open_notepad");
const Close_notepad = document.querySelector(".close_notepad");
const Notepad = document.querySelector(".notepad");

Open_notepad.addEventListener("click", () =>{
    Notepad.style.display = "block";
});

Close_notepad.addEventListener("click", () =>{
    Notepad.style.display = "none";
});

document.addEventListener("click", (e) =>{
    if (e.target == Notepad){
        Notepad.style.display = "none";
    }
});