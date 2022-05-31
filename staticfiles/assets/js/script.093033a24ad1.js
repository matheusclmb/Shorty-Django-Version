function copyToClipboard() {
  let copyText = document.getElementById("newurl");
  let myURL = copyText.href;
  navigator.clipboard.writeText(myURL);
}
