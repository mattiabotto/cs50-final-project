const reorderList = document.querySelector("#reorder-list");

reorderList.addEventListener("click", (e) => {
  // Assure that function triggers only when buttons are pressed
  if (e.target.tagName != "BUTTON") return;

  const btn = e.target;
  const currentRow = btn.closest("li");
  const action = btn.classList.contains("btn-up") ? "up" : "down";

  if (action == "up") {
    const previousRow = currentRow.previousElementSibling;
    previousRow.before(currentRow);
  } else {
    const nextRow = currentRow.nextElementSibling;
    nextRow.after(currentRow);
  }
});
