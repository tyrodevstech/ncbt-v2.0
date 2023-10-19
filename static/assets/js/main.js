// Cache frequently used elements
const $menuToggleBtns = $(".menu-toggle-btn");
const $navToggleBtn = $(".nav-toggle-btn");
const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
const preloader = document.querySelector(".preloader-main");

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


document.addEventListener("DOMContentLoaded", (event) => {
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
  const header_slider = new Swiper("#header-slider", {
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

  const student_facilities_slider = new Swiper("#student-facilities-slider", {
    pagination: {
      el: ".swiper-pagination",
    },
    slidesPerView: 1,
    spaceBetween: 30,
    breakpoints: {
      // when window width is >= 480px
      576: {
        slidesPerView: 2,
      },
      // when window width is >= 640px
      768: {
        slidesPerView: 3,
      },
    },
  });

  const advisor_slider = new Swiper("#advisor-slider", {
    pagination: {
      el: ".swiper-pagination",
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    slidesPerView: 1,
    spaceBetween: 30,
    breakpoints: {
      // when window width is >= 480px
      576: {
        slidesPerView: 2,
      },
      // when window width is >= 640px
      768: {
        slidesPerView: 3,
      },
      992: {
        slidesPerView: 4,
      },
    },
  });

  function scrollWaypointInit(items, trigger) {
    items.each(function () {
      var element = $(this),
        osAnimationClass = element.data("animation"),
        osAnimationDelay = element.attr("data-animation-delay");

      element.css({
        "-webkit-animation-delay": osAnimationDelay,
        "-moz-animation-delay": osAnimationDelay,
        "animation-delay": osAnimationDelay,
      });

      var trigger = trigger ? trigger : element;

      trigger.waypoint(
        function () {
          element.addClass(osAnimationClass);
        },
        {
          triggerOnce: true,
          offset: "80%",
        }
      );
    });
  }

  //Call the init
  // scrollWaypointInit($(".animate__animated"));

  $(".popup-image").magnificPopup({
    type: "image",
    mainClass: "mfp-fade",
    callbacks: {
      elementParse: function (item) {
        item.src = item.el.attr("src");
      },
    },
  });

  new PureCounter({
    selector: ".counter",
    start: 0,
    // end: 100,
    duration: 2,
    delay: 20,
    // once: false,
    // repeat: false,
    // decimals: 0,
    legacy: true,
    filesizing: false,
    currency: false,
    separator: false,
  });

});


window.addEventListener("load", (event) => {
  hidePreloader();

});


// Automatically hide preloader after 5 seconds
setTimeout(hidePreloader, 5000);