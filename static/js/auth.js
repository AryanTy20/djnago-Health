const stu = document.querySelector("#student");
const doc = document.querySelector("#doctor");
const stuForm = document.querySelector(".studentRegBox");
const docForm = document.querySelector(".doctorRegBox");

doc.addEventListener("click", () => {
  stu.classList.remove("activeTab");
  doc.classList.add("activeTab");
  stuForm.classList.add("hideStudent");
  docForm.classList.add("showDoctor");
});

stu.addEventListener("click", () => {
  doc.classList.remove("activeTab");
  stu.classList.add("activeTab");
  stuForm.classList.remove("hideStudent");
  docForm.classList.remove("showDoctor");
});
