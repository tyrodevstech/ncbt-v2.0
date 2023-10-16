// Cache frequently used elements
const $menuToggleBtns = $(".menu-toggle-btn");
const $navToggleBtn = $(".nav-toggle-btn");
const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
const preloader = document.querySelector(".preloader");

// Function to handle preloader animation
function hidePreloader() {
  gsap.to(preloader, {
    ease: Power1.easeOut,
    opacity: 0,
    display: "none",
    duration: 1,
  });
  document.body.style.overflowY = "unset";
}

// Hide preloader on page load
window.addEventListener("load", (event) => {
  // Click event handler for menu toggle buttons
  $menuToggleBtns.on("click", function () {
    const $dropdownEl = $(this).parent();
    const strategy = $dropdownEl.css("--strategy") || "static";
    if (strategy.trim() !== "static") return;
    $(this).next("ul").toggleClass("menu-open");
  });

  // Click event handler for nav toggle button
  $navToggleBtn.on("click", function () {
    $(this).find("i").toggleClass("ti-x");
    $("#navbar").toggleClass("nav-open");
  });

  // Initialize Swiper for header slider
  new Swiper("#header-slider", {
    preloadImages: false,
    lazy: true,
    centeredSlides: true,
    autoplay: {
      delay: 6000,
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    keyboard: true,
    on: {
      autoplayTimeLeft(s, time, progress) {
        progressCircle.style.setProperty("--progress", 1 - progress);
        progressContent.textContent = `${Math.ceil(time / 1000)}s`;
      },
    },
  });

  // Initialize Swiper for testimonial slider
  new Swiper(".testimonial-slider", {
    preloadImages: false,
    lazy: true,
    centeredSlides: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    keyboard: true,
  });

  $(".open-popup-link").magnificPopup({
    type: "iframe",
    midClick: true,
    mainClass: "mfp-fade",
  });

  hidePreloader();
});

// Automatically hide preloader after 5 seconds
setTimeout(hidePreloader, 5000);
