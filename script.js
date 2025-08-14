// CounterCore HazardAV JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
            
            // Close mobile menu if open
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
            }
        });
    });
    
    // Header Background on Scroll
    const header = document.querySelector('.header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            header.style.background = 'rgba(10, 10, 10, 0.95)';
        }
    });
    
    // Intersection Observer for Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.feature-card, .pricing-card, .gaming-feature, .enterprise-feature');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Enhanced Button Interactions
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        button.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('div');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                pointer-events: none;
                transform: scale(0);
                animation: ripple 0.6s linear;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Add ripple animation keyframes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Pricing Card Hover Effects
    const pricingCards = document.querySelectorAll('.pricing-card');
    pricingCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 15px 40px rgba(220, 38, 38, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            if (this.classList.contains('premium')) {
                this.style.transform = 'translateY(0) scale(1.05)';
            } else {
                this.style.transform = 'translateY(0) scale(1)';
            }
            this.style.boxShadow = 'none';
        });
    });
    
    // Gaming Demo Interaction
    const demoWindow = document.querySelector('.demo-window');
    if (demoWindow) {
        const notificationActions = document.querySelectorAll('.notification-actions .btn');
        notificationActions.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const action = this.textContent.trim();
                
                // Simulate different responses
                let message = '';
                let messageClass = '';
                
                switch(action) {
                    case 'Permitir':
                        message = '✅ Archivo permitido - Agregado a lista de confianza';
                        messageClass = 'success';
                        break;
                    case 'Bloquear':
                        message = '🛡️ Archivo bloqueado - Movido a cuarentena';
                        messageClass = 'danger';
                        break;
                    case 'Más Info':
                        message = '📊 Mostrando análisis detallado...';
                        messageClass = 'info';
                        break;
                }
                
                // Show feedback
                const feedback = document.createElement('div');
                feedback.className = `demo-feedback ${messageClass}`;
                feedback.textContent = message;
                feedback.style.cssText = `
                    position: absolute;
                    top: 10px;
                    right: 10px;
                    background: var(--card-bg);
                    border: 1px solid var(--border-glow);
                    border-radius: 8px;
                    padding: 0.5rem 1rem;
                    font-size: 0.9rem;
                    z-index: 10;
                    animation: slideIn 0.3s ease;
                `;
                
                demoWindow.style.position = 'relative';
                demoWindow.appendChild(feedback);
                
                setTimeout(() => {
                    feedback.remove();
                }, 3000);
            });
        });
    }
    
    // Add slide-in animation
    const slideInStyle = document.createElement('style');
    slideInStyle.textContent = `
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(100%);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .demo-feedback.success {
            border-color: var(--success-green);
            color: var(--success-green);
        }
        
        .demo-feedback.danger {
            border-color: var(--primary-red);
            color: var(--primary-red);
        }
        
        .demo-feedback.info {
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }
    `;
    document.head.appendChild(slideInStyle);
    
    // Download Button Functionality
    const downloadButtons = document.querySelectorAll('.btn-primary');
    downloadButtons.forEach(btn => {
        if (btn.textContent.includes('Descargar')) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Simulate download process
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Preparando descarga...';
                this.disabled = true;
                
                setTimeout(() => {
                    this.innerHTML = '<i class="fas fa-check"></i> ¡Próximamente disponible!';
                    
                    setTimeout(() => {
                        this.innerHTML = originalText;
                        this.disabled = false;
                    }, 2000);
                }, 1500);
            });
        }
    });
    
    // Contact/Premium buttons
    const contactButtons = document.querySelectorAll('.btn');
    contactButtons.forEach(btn => {
        if (btn.textContent.includes('Obtener Premium') || btn.textContent.includes('Contactar')) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Simulate contact/premium action
                const modal = document.createElement('div');
                modal.style.cssText = `
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.8);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                    backdrop-filter: blur(5px);
                `;
                
                const modalContent = document.createElement('div');
                modalContent.style.cssText = `
                    background: var(--card-bg);
                    border: 1px solid var(--border-glow);
                    border-radius: 12px;
                    padding: 2rem;
                    max-width: 400px;
                    text-align: center;
                    animation: modalSlide 0.3s ease;
                `;
                
                modalContent.innerHTML = `
                    <h3 style="color: var(--text-primary); margin-bottom: 1rem;">🚀 ¡Próximamente!</h3>
                    <p style="color: var(--text-secondary); margin-bottom: 2rem;">CounterCore HazardAV está en desarrollo. ¡Mantente atento para el lanzamiento!</p>
                    <button class="btn btn-primary" onclick="this.closest('.modal').remove()">Entendido</button>
                `;
                
                modal.className = 'modal';
                modal.appendChild(modalContent);
                document.body.appendChild(modal);
                
                // Close on backdrop click
                modal.addEventListener('click', function(e) {
                    if (e.target === modal) {
                        modal.remove();
                    }
                });
            });
        }
    });
    
    // Add modal animation
    const modalStyle = document.createElement('style');
    modalStyle.textContent = `
        @keyframes modalSlide {
            from {
                opacity: 0;
                transform: translateY(-50px) scale(0.9);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
    `;
    document.head.appendChild(modalStyle);
    
    // Return to main ecosystem functionality
    window.returnToEcosystem = function() {
        // Send message to parent window to close this view
        if (window.parent && window.parent !== window) {
            window.parent.postMessage('hideCounterCore', '*');
        }
    };
    
    console.log('🛡️ CounterCore HazardAV initialized successfully!');
});
