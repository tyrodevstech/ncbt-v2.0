/**
 * Toast Types
 * Different toast types with their properties.
 */
const toastTypes = {
  info: {
    bgColor: "bg-indigo-500",
    bgProgressColor: "bg-indigo-700",
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-info-triangle" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0z"></path>
        <path d="M12 9h.01"></path>
        <path d="M11 12h1v4h1"></path>
      </svg>`,
  },
  warn: {
    bgColor: "bg-orange-400",
    bgProgressColor: "bg-orange-600",
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-alert-circle" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"></path>
        <path d="M12 8v4"></path>
        <path d="M12 16h.01"></path>
      </svg>`,
  },
  error: {
    bgColor: "bg-rose-500",
    bgProgressColor: "bg-rose-700",
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-alert-triangle" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M12 9v4"></path>
        <path d="M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0z"></path>
        <path d="M12 16h.01"></path>
      </svg>`,
  },
  success: {
    bgColor: "bg-teal-500",
    bgProgressColor: "bg-teal-700",
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-checkbox" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M9 11l3 3l8 -8"></path>
        <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
      </svg>`,
  },
  default: {
    bgColor: "bg-gray-500",
    bgProgressColor: "bg-gray-700",
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-bell-ringing" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M10 5a2 2 0 0 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3h-16a4 4 0 0 0 2 -3v-3a7 7 0 0 1 4 -6"></path>
        <path d="M9 17v1a3 3 0 0 0 6 0v-1"></path>
        <path d="M21 6.727a11.05 11.05 0 0 0 -2.794 -3.727"></path>
        <path d="M3 6.727a11.05 11.05 0 0 1 2.792 -3.727"></path>
      </svg>`,
  },
};

/**
 * Common Toast Class
 * CSS classes shared among all toast elements.
 */
const commonToastClass =
  "toast mb-4 last:mb-0 flex p-4 text-white overflow-hidden duration-200 relative shadow-xl justify-between rounded transition-all sm:w-80 w-auto opacity-0";

/**
 * Create Toast Element
 * Creates a new toast element with given title, message, toastType, and close button.
 *
 * @param {string} title - Title of the toast.
 * @param {string} message - Message of the toast.
 * @param {object} toastType - Toast type properties.
 * @param {boolean} showCloseButton - Whether to show a close button.
 * @returns {HTMLElement} - Toast element.
 */
function createToastElement(title, message, toastType, showCloseButton) {
  if (toastType == "info") toastType = toastTypes.info;
  else if (toastType == "warn") toastType = toastTypes.warn;
  else if (toastType == "success") toastType = toastTypes.success;
  else if (toastType == "error") toastType = toastTypes.error;
  else toastType = toastTypes.default;

  const toastElement = document.createElement("div");
  toastElement.className = `${commonToastClass} ${toastType.bgColor}`;
  // Create icon element
  const iconDiv = document.createElement("div");
  iconDiv.className = "flex items-center";
  iconDiv.innerHTML = toastType.icon;
  toastElement.appendChild(iconDiv);

  // Create content element
  const contentDiv = document.createElement("div");
  contentDiv.className = "ml-4 mr-2 w-full flex flex-col justify-center";
  contentDiv.innerHTML = `<h1 class="font-semibold leading-none -mt-0.5 title">${title}</h1>
                            ${
                              message
                                ? `<p class="text-sm message mt-1">${message}</p>`
                                : ""
                            }`;
  toastElement.appendChild(contentDiv);

  // Create close button if necessary
  if (showCloseButton) {
    const closeDiv = document.createElement("div");
    closeDiv.className = `flex ${
      message ? "" : "items-center"
    } cursor-pointer close-button`;
    closeDiv.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x w-4 h-4" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M18 6l-12 12"></path>
                            <path d="M6 6l12 12"></path>
                          </svg>`;
    toastElement.appendChild(closeDiv);
  }

  // Create progress bar
  const progressBar = document.createElement("div");
  progressBar.className = `h-0.5 w-[calc(100%*var(--progress))] ${toastType.bgProgressColor} progress absolute bottom-0 inset-x-0`;
  toastElement.appendChild(progressBar);

  return toastElement;
}

/**
 * Default Options
 * Default configuration options for toasts.
 */
const DEFAULT_OPTIONS = {
  position: "top-right",
  autoClose: 5000,
  onClose: () => {},
  canClose: true,
  showProgress: true,
};

/**
 * Toast Class
 * Represents a toast notification with various configuration options.
 */
class Toast {
  // Private instance variables
  #toastElem;
  #autoCloseInterval;
  #progressInterval;
  #removeBinded;
  #timeVisible = 0;
  #autoClose;
  #isPaused = false;
  #unpause;
  #pause;
  #visibilityChange;
  #shouldUnPause;

  constructor(options) {
    // Create the toast element and set initial properties
    this.#toastElem = createToastElement(
      options.title,
      options.message,
      options.toastType,
      true
    );
    this.#toastElem.classList.add("toast");
    requestAnimationFrame(() => {
      this.#toastElem.classList.add("show");
      this.#toastElem.style.opacity = 1;
    });

    // Bind functions to the current instance
    this.#removeBinded = this.remove.bind(this);
    this.#unpause = () => (this.#isPaused = false);
    this.#pause = () => (this.#isPaused = true);
    this.#visibilityChange = () => {
      this.#shouldUnPause = document.visibilityState === "visible";
    };

    // Update the toast with default and provided options
    this.update({ ...DEFAULT_OPTIONS, ...options });
  }

  set autoClose(value) {
    // Set the autoClose property and manage auto-closing behavior
    this.#autoClose = value;
    this.#timeVisible = 0;
    if (value === false) return;

    let lastTime;
    const func = (time) => {
      if (this.#shouldUnPause) {
        lastTime = null;
        this.#shouldUnPause = false;
      }
      if (lastTime == null) {
        lastTime = time;
        this.#autoCloseInterval = requestAnimationFrame(func);
        return;
      }
      if (!this.#isPaused) {
        this.#timeVisible += time - lastTime;
        if (this.#timeVisible >= this.#autoClose) {
          this.remove();
          return;
        }
      }

      lastTime = time;
      this.#autoCloseInterval = requestAnimationFrame(func);
    };

    this.#autoCloseInterval = requestAnimationFrame(func);
  }

  set position(value) {
    // Set the position property and manage the toast's container
    const currentContainer = this.#toastElem.parentElement;
    const selector = `.toast-container[data-position="${value}"]`;
    const container =
      document.querySelector(selector) || createContainer(value);
    container.append(this.#toastElem);
    if (currentContainer == null || currentContainer.hasChildNodes()) return;
    currentContainer.remove();
  }

  set canClose(value) {
    // Enable or disable the ability to close the toast on click
    this.#toastElem.classList.toggle("can-close", value);
    if (value) {
      this.#toastElem.addEventListener("click", this.#removeBinded);
    } else {
      this.#toastElem.removeEventListener("click", this.#removeBinded);
    }
  }

  set showProgress(value) {
    // Display or hide the progress bar and manage its progression
    this.#toastElem.classList.toggle("progress", value);
    this.#toastElem.style.setProperty("--progress", 1);

    if (value) {
      const func = () => {
        if (!this.#isPaused) {
          this.#toastElem.style.setProperty(
            "--progress",
            1 - this.#timeVisible / this.#autoClose
          );
        }
        this.#progressInterval = requestAnimationFrame(func);
      };

      this.#progressInterval = requestAnimationFrame(func);
    }
  }

  set pauseOnHover(value) {
    // Enable or disable pausing on hover
    if (value) {
      this.#toastElem.addEventListener("mouseover", this.#pause);
      this.#toastElem.addEventListener("mouseleave", this.#unpause);
    } else {
      this.#toastElem.removeEventListener("mouseover", this.#pause);
      this.#toastElem.removeEventListener("mouseleave", this.#unpause);
    }
  }

  set pauseOnFocusLoss(value) {
    // Enable or disable pausing on focus loss
    if (value) {
      document.addEventListener("visibilitychange", this.#visibilityChange);
    } else {
      document.removeEventListener("visibilitychange", this.#visibilityChange);
    }
  }

  update(options) {
    // Update multiple properties at once using an options object
    Object.entries(options).forEach(([key, value]) => {
      this[key] = value;
    });
  }

  remove() {
    // Remove the toast and handle animations and cleanup
    cancelAnimationFrame(this.#autoCloseInterval);
    cancelAnimationFrame(this.#progressInterval);
    const container = this.#toastElem.parentElement;
    this.#toastElem.style.opacity = 0;
    this.#toastElem.addEventListener("transitionend", () => {
      this.#toastElem.remove();
      if (container.hasChildNodes()) return;
      container.remove();
    });
    this.onClose();
  }
}

/**
 * Create Toast Container
 * Creates and appends a new container for toast elements based on their position.
 *
 * @param {string} position - Position where the container should be created.
 * @returns {HTMLElement} - Toast container element.
 */
function createContainer(position) {
  const container = document.createElement("div");
  container.className = `toast-container fixed z-[9999] ${
    position.startsWith("top-") ? "top-4" : ""
  } ${position.startsWith("bottom-") ? "bottom-4" : ""} ${
    position.endsWith("-right") ? "right-4" : ""
  } ${position.endsWith("-left") ? "left-4" : ""}`;
  container.dataset.position = position;
  document.body.append(container);
  return container;
}
