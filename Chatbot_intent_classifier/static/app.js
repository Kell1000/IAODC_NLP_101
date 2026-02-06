/**
 * Kella Chatbot - Enhanced Interactive Chat Experience
 * Features: Typing indicators, animations, welcome message, timestamps
 */

// ==========================================
// DYNAMIC BACKGROUND ANIMATION
// ==========================================
class ParticleNetwork {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.particles = [];
        this.numParticles = 100; // Default count
        this.mouse = { x: null, y: null, radius: 150 };

        this.resize();
        this.init();
        this.animate();

        // Event Listeners
        window.addEventListener('resize', () => this.resize());
        this.canvas.addEventListener('mousemove', (e) => this.mouseMove(e));
        this.canvas.addEventListener('mouseout', () => {
            this.mouse.x = null;
            this.mouse.y = null;
        });
    }

    resize() {
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;

        // Adjust particle count for mobile
        if (this.width < 768) {
            this.numParticles = 50;
        } else {
            this.numParticles = 100;
        }

        // Re-init if particles are too few/many (optional, but good for heavy resizes)
        if (this.particles.length === 0) this.init();
    }

    init() {
        this.particles = [];
        for (let i = 0; i < this.numParticles; i++) {
            this.particles.push(new Particle(this.width, this.height));
        }
    }

    mouseMove(e) {
        const rect = this.canvas.getBoundingClientRect();
        this.mouse.x = e.clientX - rect.left;
        this.mouse.y = e.clientY - rect.top;
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        this.ctx.clearRect(0, 0, this.width, this.height);

        for (let i = 0; i < this.particles.length; i++) {
            this.particles[i].update(this.mouse);
            this.particles[i].draw(this.ctx);

            // Draw connections
            for (let j = i; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 100) {
                    this.ctx.beginPath();
                    this.ctx.strokeStyle = `rgba(167, 139, 250, ${1 - distance / 100})`;
                    this.ctx.lineWidth = 1;
                    this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
                    this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
                    this.ctx.stroke();
                }
            }
        }
    }
}

class Particle {
    constructor(canvasWidth, canvasHeight) {
        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;
        this.x = Math.random() * canvasWidth;
        this.y = Math.random() * canvasHeight;
        this.directionX = (Math.random() * 0.4) - 0.2;
        this.directionY = (Math.random() * 0.4) - 0.2;
        this.size = (Math.random() * 2) + 1;
        this.color = '#a78bfa';
    }

    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();

        // Glow effect
        ctx.shadowBlur = 10;
        ctx.shadowColor = this.color;
    }

    update(mouse) {
        // Boundary check
        if (this.x > this.canvasWidth || this.x < 0) {
            this.directionX = -this.directionX;
        }
        if (this.y > this.canvasHeight || this.y < 0) {
            this.directionY = -this.directionY;
        }

        // Mouse interaction
        let mouseDx = mouse.x - this.x;
        let mouseDy = mouse.y - this.y;
        let distance = Math.sqrt(mouseDx * mouseDx + mouseDy * mouseDy);

        if (distance < mouse.radius && mouse.x !== null) {
            if (mouse.x < this.x && this.x < this.canvasWidth - 10) {
                this.x += 1;
            }
            if (mouse.x > this.x && this.x > 10) {
                this.x -= 1;
            }
            if (mouse.y < this.y && this.y < this.canvasHeight - 10) {
                this.y += 1;
            }
            if (mouse.y > this.y && this.y > 10) {
                this.y -= 1;
            }
        }

        // Move
        this.x += this.directionX;
        this.y += this.directionY;
    }
}

// ==========================================
// CHATBOT LOGIC
// ==========================================
class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        };

        this.state = false;
        this.messages = [];
        this.isFirstOpen = true;
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox);
            }
        });
    }

    toggleState(chatbox) {
        this.state = !this.state;

        if (this.state) {
            chatbox.classList.add('chatbox--active');

            // Show welcome message on first open
            if (this.isFirstOpen) {
                this.showWelcomeMessage(chatbox);
                this.isFirstOpen = false;
            }

            // Focus input
            setTimeout(() => {
                chatbox.querySelector('input').focus();
            }, 300);
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }

    showWelcomeMessage(chatbox) {
        const welcomeMessages = [
            "👋 Hello! Welcome to Kella!",
            "I'm your AI shopping assistant. I can help you with:",
            "🛒 Product recommendations",
            "📦 Order tracking & shipping info",
            "❓ Any questions you have!",
            "",
            "How can I assist you today?"
        ];

        // Add welcome messages with delay
        let delay = 0;
        welcomeMessages.forEach((msg, index) => {
            if (msg) {
                setTimeout(() => {
                    let welcomeMsg = { name: "Sam", message: msg };
                    this.messages.push(welcomeMsg);
                    this.updateChatText(chatbox);
                }, delay);
                delay += 400;
            }
        });
    }

    onSendButton(chatbox) {
        const textField = chatbox.querySelector('input');
        const text1 = textField.value.trim();

        if (text1 === "") {
            return;
        }

        // Add user message
        const msg1 = { name: "User", message: text1, time: this.getTime() };
        this.messages.push(msg1);
        this.updateChatText(chatbox);
        textField.value = '';

        // Show typing indicator
        this.showTypingIndicator(chatbox);

        // Send to server
        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(r => r.json())
            .then(r => {
                this.hideTypingIndicator(chatbox);
                const msg2 = { name: "Sam", message: r.answer, time: this.getTime() };
                this.messages.push(msg2);
                this.updateChatText(chatbox);
            })
            .catch((error) => {
                console.error('Error:', error);
                this.hideTypingIndicator(chatbox);
                const errorMsg = {
                    name: "Sam",
                    message: "I'm having trouble connecting. Please try again in a moment! 🔄",
                    time: this.getTime()
                };
                this.messages.push(errorMsg);
                this.updateChatText(chatbox);
            });
    }

    showTypingIndicator(chatbox) {
        const messagesContainer = chatbox.querySelector('.chatbox__messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'messages__item messages__item--typing typing-indicator-container';
        typingDiv.innerHTML = `
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;
        messagesContainer.insertBefore(typingDiv, messagesContainer.firstChild);
    }

    hideTypingIndicator(chatbox) {
        const typingIndicator = chatbox.querySelector('.typing-indicator-container');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    getTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    updateChatText(chatbox) {
        let html = '';

        this.messages.slice().reverse().forEach((item, index) => {
            if (item.name === "Sam") {
                html += `
                    <div class="messages__item messages__item--visitor">
                        ${this.formatMessage(item.message)}
                    </div>
                `;
            } else {
                html += `
                    <div class="messages__item messages__item--operator">
                        ${this.formatMessage(item.message)}
                    </div>
                `;
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

    formatMessage(message) {
        // Convert URLs to links
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        message = message.replace(urlRegex, '<a href="$1" target="_blank" rel="noopener" style="color: #a78bfa; text-decoration: underline;">$1</a>');

        // Convert phone numbers to tel links
        const phoneRegex = /(\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9})/g;
        message = message.replace(phoneRegex, '<a href="tel:$1" style="color: #a78bfa;">$1</a>');

        return message;
    }
}

// Initialize chatbox and background when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Init Chatbox
    const chatbox = new Chatbox();
    chatbox.display();

    // Init Background Animation
    const heroCanvas = document.getElementById('hero-canvas');
    if (heroCanvas) {
        const particleNetwork = new ParticleNetwork('hero-canvas');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});