/**
 * HARRISON BARROW, ATTORNEY AT LAW P.C.
 * Global JavaScript Behaviors
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeaderScroll();
  initMobileMenu();
  initScrollReveal();
  initSliders();
  initFormValidation();
  initResultsFilter();
});

/**
 * 1. Shrink header on page scroll
 */
function initHeaderScroll() {
  const header = document.getElementById('header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  // Run on load and add event listener
  handleScroll();
  window.addEventListener('scroll', handleScroll);
}

/**
 * 2. Mobile Menu Toggler & Dropdown submenus
 */
function initMobileMenu() {
  const navToggle = document.getElementById('nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  const dropdownToggle = document.querySelector('.nav-item-dropdown');

  if (!navToggle || !navMenu) return;

  // Toggle active state on hamburger click
  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.contains('open');
    if (isOpen) {
      navMenu.classList.remove('open');
      navToggle.classList.remove('open');
      document.body.style.overflow = '';
    } else {
      navMenu.classList.add('open');
      navToggle.classList.add('open');
      document.body.style.overflow = 'hidden'; // Lock background scrolling
    }
  });

  // Mobile submenu accordion
  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        // Toggle the open class for mobile views
        dropdownToggle.classList.toggle('open');
      }
    });
  }

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (navMenu.classList.contains('open') && !navMenu.contains(e.target) && !navToggle.contains(e.target)) {
      navMenu.classList.remove('open');
      navToggle.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}

/**
 * 3. Intersection Observer for Scroll Reveals
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          // Once it reveals, we don't need to observe it anymore
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(element => {
      observer.observe(element);
    });
  } else {
    // Fallback for older browsers
    revealElements.forEach(element => {
      element.classList.add('active');
    });
  }
}

/**
 * 4. Sliders (Testimonials and Case Results)
 */
function initSliders() {
  const sliders = document.querySelectorAll('.slider-container');
  
  sliders.forEach(slider => {
    const track = slider.querySelector('.slider-track');
    const prevBtn = slider.querySelector('.slider-prev');
    const nextBtn = slider.querySelector('.slider-next');
    
    if (!track) return;
    
    let currentIndex = 0;
    const slides = Array.from(track.children);
    if (slides.length === 0) return;
    
    // Determine how many slides are shown at once based on viewport
    const getSlidesVisible = () => {
      const width = window.innerWidth;
      if (track.classList.contains('results-slider-track')) {
        if (width >= 1024) return 3;
        if (width >= 768) return 2;
      }
      return 1;
    };
    
    const updateSlider = () => {
      const slidesVisible = getSlidesVisible();
      const maxIndex = Math.max(0, slides.length - slidesVisible);
      
      if (currentIndex > maxIndex) currentIndex = maxIndex;
      if (currentIndex < 0) currentIndex = 0;
      
      // Calculate transform offset
      const offset = -(currentIndex * (100 / slidesVisible));
      track.style.transform = `translateX(${offset}%)`;
      
      // Disable buttons at boundaries
      if (prevBtn) prevBtn.style.opacity = currentIndex === 0 ? '0.3' : '1';
      if (nextBtn) nextBtn.style.opacity = currentIndex === maxIndex ? '0.3' : '1';
    };
    
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
          currentIndex--;
          updateSlider();
        }
      });
    }
    
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const slidesVisible = getSlidesVisible();
        const maxIndex = slides.length - slidesVisible;
        if (currentIndex < maxIndex) {
          currentIndex++;
          updateSlider();
        }
      });
    }
    
    // Auto slider for testimonials
    if (slider.classList.contains('testimonials-slider')) {
      setInterval(() => {
        const slidesVisible = getSlidesVisible();
        const maxIndex = slides.length - slidesVisible;
        if (currentIndex < maxIndex) {
          currentIndex++;
        } else {
          currentIndex = 0;
        }
        updateSlider();
      }, 7000); // 7 seconds per slide
    }
    
    // Run on load and on resize
    window.addEventListener('resize', updateSlider);
    updateSlider();
  });
}

/**
 * 5. Client-Side Contact Form Validation
 */
function initFormValidation() {
  const forms = document.querySelectorAll('.validated-form');
  
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      let isValid = true;
      const requiredInputs = form.querySelectorAll('[required]');
      
      requiredInputs.forEach(input => {
        // Simple empty checks
        if (!input.value.trim()) {
          showInputError(input, 'This field is required.');
          isValid = false;
        } else {
          clearInputError(input);
        }
        
        // Email pattern check
        if (input.type === 'email' && input.value.trim()) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(input.value.trim())) {
            showInputError(input, 'Please enter a valid email address.');
            isValid = false;
          }
        }
        
        // Phone pattern check
        if (input.type === 'tel' && input.value.trim()) {
          const digits = input.value.replace(/\D/g, '');
          if (digits.length < 10) {
            showInputError(input, 'Please enter a valid phone number (min 10 digits).');
            isValid = false;
          }
        }
      });
      
      // Submit via AJAX so we can send the visitor to our own Thank-You page.
      // (Formspree's free plan otherwise shows its generic "Thanks" page.)
      e.preventDefault();
      if (!isValid) return;

      var btn = form.querySelector('[type="submit"]');
      var originalText = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.innerHTML = 'Sending\u2026'; }

      var nextField = form.querySelector('input[name="_next"]');
      var next = (nextField && nextField.value) ? nextField.value : '/thank-you/';

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function (response) {
        if (response.ok) {
          window.location.href = next;
        } else {
          return response.json().then(function (data) {
            var msg = (data && data.errors)
              ? data.errors.map(function (er) { return er.message; }).join(', ')
              : 'There was a problem sending your message.';
            throw new Error(msg);
          });
        }
      }).catch(function (err) {
        if (btn) { btn.disabled = false; btn.innerHTML = originalText; }
        alert((err && err.message ? err.message : 'Something went wrong.') + ' You can also call (508) 945-1400.');
      });
    });
  });
}

function showInputError(input, message) {
  let errorDisplay = input.parentNode.querySelector('.form-error-message');
  
  if (!errorDisplay) {
    errorDisplay = document.createElement('span');
    errorDisplay.className = 'form-error-message';
    errorDisplay.style.color = '#ef4444';
    errorDisplay.style.fontSize = '0.75rem';
    errorDisplay.style.marginTop = '0.25rem';
    errorDisplay.style.display = 'block';
    input.parentNode.appendChild(errorDisplay);
  }
  
  errorDisplay.textContent = message;
  input.style.borderColor = '#ef4444';
}

function clearInputError(input) {
  const errorDisplay = input.parentNode.querySelector('.form-error-message');
  if (errorDisplay) {
    errorDisplay.remove();
  }
  input.style.borderColor = '';
}

/**
 * 6. Case Results Filtering Logic (Directory Page)
 */
function initResultsFilter() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.results-grid .result-card, .results-grid-container .result-card');
  
  if (filterButtons.length === 0 || cards.length === 0) return;
  
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Toggle active classes
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      const filterValue = btn.getAttribute('data-filter');
      
      cards.forEach(card => {
        // Find tags inside card
        const tag = card.getAttribute('data-category') || '';
        
        if (filterValue === 'all' || tag.toLowerCase() === filterValue.toLowerCase()) {
          card.style.display = 'flex';
          // Force active class for transition
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.95)';
          // Wait for transition before hiding
          setTimeout(() => {
            card.style.display = 'none';
          }, 300);
        }
      });
    });
  });
}