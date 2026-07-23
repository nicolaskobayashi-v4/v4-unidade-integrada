(() => {
  "use strict";

  const siteHeader = document.querySelector(".site-header");
  const menuButton = document.querySelector(".menu-toggle");
  const mobileMenu = document.querySelector("#mobile-menu");

  const updateHeaderState = () => {
    siteHeader?.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateHeaderState();
  window.addEventListener("scroll", updateHeaderState, { passive: true });

  if (!menuButton || !mobileMenu) {
    return;
  }

  const setMenuState = (isOpen) => {
    menuButton.setAttribute("aria-expanded", String(isOpen));
    menuButton.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
    mobileMenu.hidden = !isOpen;
  };

  menuButton.addEventListener("click", () => {
    const isOpen = menuButton.getAttribute("aria-expanded") === "true";
    setMenuState(!isOpen);
  });

  mobileMenu.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      setMenuState(false);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      setMenuState(false);
      menuButton.focus();
    }
  });

  const desktopQuery = window.matchMedia("(min-width: 68.0625rem)");

  const closeMenuAtDesktop = (event) => {
    if (event.matches) {
      setMenuState(false);
    }
  };

  desktopQuery.addEventListener("change", closeMenuAtDesktop);
})();
