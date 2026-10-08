(function () {
  'use strict';

  /* Navbar: blur on scroll + mobile menu */
  var navbar = document.getElementById('navbar');
  var burger = document.getElementById('burger');
  var navLinks = document.getElementById('navLinks');

  function onScroll() { navbar.classList.toggle('scrolled', window.scrollY > 20); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  burger.addEventListener('click', function () {
    var open = navLinks.classList.toggle('open');
    burger.setAttribute('aria-expanded', String(open));
  });
  navLinks.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      navLinks.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });

  /* Fade-in on scroll */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.1 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* Project filtering */
  var filterBtns = document.querySelectorAll('.filter');
  var projects = document.querySelectorAll('.project');

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.dataset.filter;
      filterBtns.forEach(function (b) { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');

      projects.forEach(function (card) {
        var match = f === 'all' || card.dataset.cat.split(' ').indexOf(f) !== -1;
        if (match) {
          card.style.display = '';
          requestAnimationFrame(function () { card.classList.remove('hide'); });
        } else {
          card.classList.add('hide');
          setTimeout(function () {
            if (card.classList.contains('hide')) card.style.display = 'none';
          }, 300);
        }
      });
    });
  });

  /* Certificate modal */
  var modal = document.getElementById('certModal');
  var certImg = document.getElementById('certImg');
  var certTitle = document.getElementById('certTitle');
  var certMissing = document.getElementById('certMissing');
  var closeBtn = document.getElementById('modalClose');
  var lastFocus = null;

  function openModal(src, title) {
    lastFocus = document.activeElement;
    certTitle.textContent = title;
    if (src) {
      certImg.alt = title + ' certificate';
      certImg.src = src;
      certImg.hidden = false;
      certMissing.hidden = true;
    } else {
      certImg.hidden = true;
      certImg.removeAttribute('src');
      certMissing.hidden = false;
    }
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }
  function closeModal() {
    modal.hidden = true;
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  }

  document.querySelectorAll('.cert').forEach(function (c) {
    c.addEventListener('click', function () { openModal(c.dataset.img, c.dataset.title); });
  });
  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', function (e) { if (e.target === modal) closeModal(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.hidden) closeModal();
  });
})();
