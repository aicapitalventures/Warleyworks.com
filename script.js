"use strict";
(() => {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector("#main-nav");
  const form = document.querySelector("#estimate-form");
  const message = document.querySelector("#form-message");
  const year = document.querySelector("#year");
  if (year) year.textContent = String(new Date().getFullYear());

  if (toggle && nav) {
    const setOpen = open => {
      nav.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
    };
    toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
    nav.querySelectorAll("a").forEach(link => link.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", event => {
      if (event.key === "Escape") setOpen(false);
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 860) setOpen(false);
    });
  }

  if (form && message) {
    const fields = [...form.querySelectorAll("input,select,textarea")];
    fields.forEach(field => field.addEventListener("input", () => {
      field.removeAttribute("aria-invalid");
      message.hidden = true;
    }));
    form.addEventListener("submit", event => {
      event.preventDefault(); // Never send or persist personal data in the preview.
      const invalid = fields.find(field => !field.checkValidity());
      if (invalid) {
        invalid.setAttribute("aria-invalid", "true");
        invalid.focus();
        message.textContent = "Please complete the highlighted field with valid information. This is still a demo: no request can be sent.";
        message.hidden = false;
        return;
      }
      message.textContent = "Preview confirmed: the form fields are valid. No information was sent or stored. Warley Works will enable real estimate requests only after a secure delivery service and business contact are verified.";
      message.hidden = false;
    });
  }
})();