// app.js — the web tier's Web Components: pt-copy + the data-pt-path navigation delegation (web-brief §4 route 1; the design §5 — authored source per R9/R10)
class PtCopy extends HTMLElement {
  connectedCallback() {
    const value = this.getAttribute("value") ?? "";
    const label = this.getAttribute("label") ?? "Copy";
    const button = document.createElement("sl-button");
    button.textContent = label;
    button.addEventListener("click", () => {
      navigator.clipboard.writeText(value);
      button.textContent = "Copied";
      window.setTimeout(() => { button.textContent = label; }, 2000);
    });
    this.replaceChildren(button);
  }
}
customElements.define("pt-copy", PtCopy);
document.addEventListener("submit", (event) => {
  const form = event.target;
  const path = form.getAttribute("data-pt-path");
  if (path === null) { return; }
  event.preventDefault();
  const stem = form.querySelector("input[name='stem']").value.trim();
  if (stem) { window.location.assign(path.replace("{stem}", encodeURIComponent(stem))); }
});
