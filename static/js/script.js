/* ==========================================================================
   script.js - all the interactive features of the portfolio
   1 Page loader        2 Theme toggle       3 Mobile menu
   4 Navbar + progress  5 Active nav link    6 Typing effect
   7 Scroll reveal      8 Skill bars         9 Counters
   10 Project filter    11 Back to top       12 Background particles
   13 Contact form
   ========================================================================== */

(function () {
    "use strict";

    var root = document.documentElement;
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* ---------- 1. PAGE LOADER ---------- */
    var loader = document.getElementById("loader");
    function hideLoader() {
        if (loader) { loader.classList.add("hidden"); }
    }
    window.addEventListener("load", function () { setTimeout(hideLoader, 600); });
    setTimeout(hideLoader, 4000); // safety net if something loads slowly

    /* ---------- 2. DARK / LIGHT THEME ---------- */
    var themeToggle = document.getElementById("themeToggle");
    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
            root.setAttribute("data-theme", next);
            try { localStorage.setItem("theme", next); } catch (e) {}
        });
    }

    /* ---------- 3. MOBILE MENU ---------- */
    var menuToggle = document.getElementById("menuToggle");
    var navLinks = document.getElementById("navLinks");

    function setMenu(open) {
        navLinks.classList.toggle("open", open);
        menuToggle.setAttribute("aria-expanded", String(open));
        menuToggle.querySelector("i").className = open ? "fa-solid fa-xmark" : "fa-solid fa-bars";
    }
    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            setMenu(!navLinks.classList.contains("open"));
        });
        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () { setMenu(false); });
        });
        document.addEventListener("keydown", function (e) {
            if (e.key === "Escape") { setMenu(false); }
        });
    }

    /* ---------- 4. NAVBAR SHADOW + SCROLL PROGRESS + 11. BACK TO TOP ---------- */
    var navbar = document.getElementById("navbar");
    var progress = document.getElementById("scrollProgress");
    var toTop = document.getElementById("toTop");

    function onScroll() {
        var y = window.scrollY || window.pageYOffset;
        var max = document.documentElement.scrollHeight - window.innerHeight;
        navbar.classList.toggle("scrolled", y > 20);
        progress.style.width = (max > 0 ? (y / max) * 100 : 0) + "%";
        toTop.classList.toggle("show", y > 500);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    toTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });

    /* ---------- 5. ACTIVE NAV LINK ---------- */
    var sections = document.querySelectorAll("main section[id]");
    var links = document.querySelectorAll(".nav-link");

    if ("IntersectionObserver" in window) {
        var navObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    links.forEach(function (link) {
                        link.classList.toggle("active", link.getAttribute("href") === "#" + entry.target.id);
                    });
                }
            });
        }, { rootMargin: "-45% 0px -50% 0px" });
        sections.forEach(function (section) { navObserver.observe(section); });
    }

    /* ---------- 6. TYPING EFFECT ---------- */
    var typedEl = document.getElementById("typed");
    if (typedEl) {
        var roles = [];
        try { roles = JSON.parse(typedEl.getAttribute("data-roles")); } catch (e) {}

        if (roles.length && !reduceMotion) {
            var roleIndex = 0, charIndex = 0, deleting = false;
            typedEl.textContent = "";

            (function type() {
                var word = roles[roleIndex];
                charIndex += deleting ? -1 : 1;
                typedEl.textContent = word.substring(0, charIndex);

                var delay = deleting ? 45 : 95;
                if (!deleting && charIndex === word.length) {
                    deleting = true;
                    delay = 1500;                       // pause on the full word
                } else if (deleting && charIndex === 0) {
                    deleting = false;
                    roleIndex = (roleIndex + 1) % roles.length;
                    delay = 400;
                }
                setTimeout(type, delay);
            })();
        }
    }

    /* ---------- 7, 8, 9. SCROLL REVEAL + SKILL BARS + COUNTERS ---------- */
    function animateCounter(el) {
        var target = parseInt(el.getAttribute("data-count"), 10) || 0;
        if (reduceMotion || target === 0) { el.textContent = target; return; }
        var current = 0;
        var step = Math.max(1, Math.round(1200 / 60 / Math.max(target, 1)));
        var timer = setInterval(function () {
            current += 1;
            el.textContent = current;
            if (current >= target) { clearInterval(timer); }
        }, step * 60);
    }

    function revealElement(el) {
        el.classList.add("visible");
        el.querySelectorAll(".bar-fill").forEach(function (bar) {
            bar.style.width = bar.getAttribute("data-level") + "%";
        });
        el.querySelectorAll("[data-count]").forEach(animateCounter);
    }

    var revealItems = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        var revealObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    revealElement(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });

        revealItems.forEach(function (item, i) {
            // tiny stagger for items in the same grid
            item.style.transitionDelay = ((i % 4) * 80) + "ms";
            revealObserver.observe(item);
            item.addEventListener("transitionend", function clear() {
                item.style.transitionDelay = "";
                item.removeEventListener("transitionend", clear);
            });
        });
    } else {
        revealItems.forEach(revealElement); // very old browsers: just show everything
    }

    /* ---------- 10. PROJECT FILTER ---------- */
    var filterButtons = document.querySelectorAll(".filter-btn");
    var projectCards = document.querySelectorAll(".project-card");

    filterButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var filter = button.getAttribute("data-filter");
            filterButtons.forEach(function (b) { b.classList.remove("active"); });
            button.classList.add("active");

            projectCards.forEach(function (card) {
                var show = filter === "all" || card.getAttribute("data-category") === filter;
                card.classList.toggle("hide", !show);
                if (show) { card.classList.add("visible"); }
            });
        });
    });

    /* ---------- 12. BACKGROUND PARTICLES ---------- */
    var canvas = document.getElementById("bgCanvas");
    if (canvas && !reduceMotion) {
        var ctx = canvas.getContext("2d");
        var width, height, points = [];
        var LINK_DISTANCE = 130;

        function resizeCanvas() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            var count = Math.min(70, Math.floor((width * height) / 22000));
            points = [];
            for (var i = 0; i < count; i++) {
                points.push({
                    x: Math.random() * width,
                    y: Math.random() * height,
                    vx: (Math.random() - 0.5) * 0.35,
                    vy: (Math.random() - 0.5) * 0.35
                });
            }
        }

        function drawParticles() {
            var light = root.getAttribute("data-theme") === "light";
            var rgb = light ? "37, 99, 235" : "96, 165, 250";
            ctx.clearRect(0, 0, width, height);

            for (var i = 0; i < points.length; i++) {
                var p = points[i];
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0 || p.x > width) { p.vx *= -1; }
                if (p.y < 0 || p.y > height) { p.vy *= -1; }

                ctx.beginPath();
                ctx.arc(p.x, p.y, 1.6, 0, Math.PI * 2);
                ctx.fillStyle = "rgba(" + rgb + ", 0.8)";
                ctx.fill();

                for (var j = i + 1; j < points.length; j++) {
                    var q = points[j];
                    var dx = p.x - q.x, dy = p.y - q.y;
                    var dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < LINK_DISTANCE) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(q.x, q.y);
                        ctx.strokeStyle = "rgba(" + rgb + "," + (0.22 * (1 - dist / LINK_DISTANCE)) + ")";
                        ctx.lineWidth = 1;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(drawParticles);
        }

        resizeCanvas();
        window.addEventListener("resize", resizeCanvas);
        drawParticles();
    }

    /* ---------- 13. CONTACT FORM ---------- */
    var form = document.getElementById("contactForm");
    if (form) {
        var statusBox = document.getElementById("formStatus");
        var submitBtn = document.getElementById("submitBtn");

        function clearErrors() {
            form.querySelectorAll(".field").forEach(function (f) { f.classList.remove("invalid"); });
            form.querySelectorAll(".error").forEach(function (e) { e.textContent = ""; });
            statusBox.className = "form-status";
            statusBox.textContent = "";
        }

        function showErrors(errors) {
            Object.keys(errors).forEach(function (field) {
                var holder = form.querySelector('[data-error-for="' + field + '"]');
                if (holder) {
                    holder.textContent = errors[field];
                    holder.closest(".field").classList.add("invalid");
                }
            });
        }

        function showStatus(type, text) {
            statusBox.className = "form-status " + type;
            statusBox.textContent = text;
        }

        form.addEventListener("submit", function (event) {
            event.preventDefault();
            clearErrors();

            // quick checks in the browser (the server checks again)
            var clientErrors = {};
            var values = {
                name: form.name.value.trim(),
                email: form.email.value.trim(),
                subject: form.subject.value.trim(),
                message: form.message.value.trim()
            };
            if (values.name.length < 2) { clientErrors.name = "Please enter your name."; }
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(values.email)) { clientErrors.email = "Please enter a valid email address."; }
            if (values.subject.length < 3) { clientErrors.subject = "Please enter a subject."; }
            if (values.message.length < 10) { clientErrors.message = "Message is too short (at least 10 characters)."; }

            if (Object.keys(clientErrors).length) {
                showErrors(clientErrors);
                showStatus("fail", "Please fix the highlighted fields.");
                return;
            }

            submitBtn.classList.add("loading");

            fetch(form.action, { method: "POST", body: new FormData(form) })
                .then(function (response) {
                    return response.json().then(function (data) { return data; });
                })
                .then(function (data) {
                    if (data.success) {
                        showStatus("success", data.message);
                        form.reset();
                    } else {
                        if (data.errors) { showErrors(data.errors); }
                        showStatus("fail", data.message || "Something went wrong. Please try again.");
                    }
                })
                .catch(function () {
                    showStatus("fail", "Could not reach the server. Please check your connection and try again.");
                })
                .then(function () {
                    submitBtn.classList.remove("loading");
                });
        });
    }
})();
