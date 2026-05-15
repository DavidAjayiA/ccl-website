// ════════════════════════════════════════════════════════════
// EXECUTIVE PAGE SCRIPTS
// ════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', function() {
  // Animation on scroll
  const animateOnScroll = () => {
    const elements = document.querySelectorAll('.anim');

    elements.forEach(el => {
      if (!el.classList.contains('visible')) {
        const rect = el.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.85) {
          const delay = el.getAttribute('data-delay') || 0;
          setTimeout(() => {
            el.classList.add('visible');
          }, delay * 100);
        }
      }
    });
  };

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Run on page load

  // Add hover effects to cards
  const coachCards = document.querySelectorAll('.coach-card');
  coachCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-6px)';
    });
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });

  const opsCards = document.querySelectorAll('.ops-card');
  opsCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-6px)';
    });
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
});
