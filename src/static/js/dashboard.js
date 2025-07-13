// Dashboard JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Audio player for previews
    const audioPlayer = document.getElementById('audio-player');
    let currentPlayingButton = null;

    // Function to play audio preview
    window.playPreview = function(previewUrl) {
        if (!previewUrl) {
            alert('No preview available for this track');
            return;
        }

        // Stop current playing audio
        if (audioPlayer.src) {
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
            if (currentPlayingButton) {
                currentPlayingButton.innerHTML = '<i class="fas fa-play"></i>';
            }
        }

        // Play new audio
        audioPlayer.src = previewUrl;
        audioPlayer.play();

        // Update button state
        const playButtons = document.querySelectorAll('.play-btn');
        playButtons.forEach(btn => {
            btn.innerHTML = '<i class="fas fa-play"></i>';
        });

        // Find the clicked button and update it
        event.target.closest('.play-btn').innerHTML = '<i class="fas fa-pause"></i>';
        currentPlayingButton = event.target.closest('.play-btn');
    };

    // Handle audio end
    audioPlayer.addEventListener('ended', function() {
        if (currentPlayingButton) {
            currentPlayingButton.innerHTML = '<i class="fas fa-play"></i>';
            currentPlayingButton = null;
        }
    });

    // Handle audio errors
    audioPlayer.addEventListener('error', function() {
        alert('Error playing audio preview');
        if (currentPlayingButton) {
            currentPlayingButton.innerHTML = '<i class="fas fa-play"></i>';
            currentPlayingButton = null;
        }
    });

    // Add click handlers for play buttons
    document.addEventListener('click', function(e) {
        if (e.target.closest('.play-btn')) {
            const button = e.target.closest('.play-btn');
            const isPlaying = button.innerHTML.includes('fa-pause');
            
            if (isPlaying) {
                // Pause audio
                audioPlayer.pause();
                button.innerHTML = '<i class="fas fa-play"></i>';
                currentPlayingButton = null;
            }
        }
    });

    // Add hover effects for track cards
    const trackCards = document.querySelectorAll('.track-card, .recommendation-card');
    trackCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Add loading states for buttons
    const spotifyButtons = document.querySelectorAll('.spotify-btn');
    spotifyButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            // Add a small loading effect
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Smooth scrolling for navigation
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Space bar to play/pause current audio
        if (e.code === 'Space' && audioPlayer.src) {
            e.preventDefault();
            if (audioPlayer.paused) {
                audioPlayer.play();
                if (currentPlayingButton) {
                    currentPlayingButton.innerHTML = '<i class="fas fa-pause"></i>';
                }
            } else {
                audioPlayer.pause();
                if (currentPlayingButton) {
                    currentPlayingButton.innerHTML = '<i class="fas fa-play"></i>';
                }
            }
        }
        
        // Escape to stop audio
        if (e.code === 'Escape' && audioPlayer.src) {
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
            if (currentPlayingButton) {
                currentPlayingButton.innerHTML = '<i class="fas fa-play"></i>';
                currentPlayingButton = null;
            }
        }
    });

    // Add tooltips for better UX
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            tooltip.style.cssText = `
                position: absolute;
                background: rgba(0, 0, 0, 0.8);
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                font-size: 12px;
                z-index: 1000;
                pointer-events: none;
                white-space: nowrap;
            `;
            
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + 'px';
            
            this.tooltip = tooltip;
        });
        
        element.addEventListener('mouseleave', function() {
            if (this.tooltip) {
                this.tooltip.remove();
                this.tooltip = null;
            }
        });
    });

    // Add mood color transitions
    const moodBadges = document.querySelectorAll('.mood-badge');
    moodBadges.forEach(badge => {
        badge.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });
        
        badge.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Add notification system
    window.showNotification = function(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#1DB954' : type === 'error' ? '#ff6b6b' : '#6495ed'};
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        `;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 3000);
    };

    // Add data attributes for better accessibility
    const playButtons = document.querySelectorAll('.play-btn');
    playButtons.forEach(btn => {
        btn.setAttribute('aria-label', 'Play preview');
        btn.setAttribute('role', 'button');
        btn.setAttribute('tabindex', '0');
    });

    const spotifyLinks = document.querySelectorAll('.spotify-btn');
    spotifyLinks.forEach(link => {
        link.setAttribute('aria-label', 'Open in Spotify');
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });

    console.log('Dashboard JavaScript loaded successfully!');
}); 