const cleanBtn = document.querySelector(".js-clean-btn");
const copyBtn = document.querySelector(".js-copy-to-clipboard-btn");

if (cleanBtn !== null) {
  cleanBtn.addEventListener("click", function () {
    document.querySelector(".js-form").reset();
  });
}

if (copyBtn !== null) {
  copyBtn.addEventListener("click", async function () {
    link = document.querySelector(".js-shorten-input").value;
    await navigator.clipboard.writeText(link);
    document.querySelector(".js-result-notification").style.display = "block";

    setTimeout(() => {
      document.querySelector(".js-result-notification").style.display = "none";
    }, 1000);
  });
}
