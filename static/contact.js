// ==================== ❄️ Efek Salju ====================
const snowCanvas = document.getElementById("snow");
const ctxSnow = snowCanvas.getContext("2d");
snowCanvas.width = window.innerWidth;
snowCanvas.height = window.innerHeight;

let snowflakes = [];

class Snowflake {
  constructor() {
    this.x = Math.random() * snowCanvas.width;
    this.y = Math.random() * snowCanvas.height;
    this.radius = Math.random() * 3 + 2;
    this.speedY = Math.random() * 1 + 0.5;
    this.speedX = (Math.random() - 0.5) * 0.5;
    this.opacity = Math.random() * 0.5 + 0.3;
  }
  update() {
    this.y += this.speedY;
    this.x += this.speedX;
    if (this.y > snowCanvas.height) {
      this.y = -this.radius;
      this.x = Math.random() * snowCanvas.width;
    }
  }
  draw() {
    let gradient = ctxSnow.createRadialGradient(
      this.x, this.y, 0,
      this.x, this.y, this.radius
    );
    gradient.addColorStop(0, `rgba(173, 216, 230, ${this.opacity})`);
    gradient.addColorStop(1, `rgba(255, 255, 255, 0)`);

    ctxSnow.beginPath();
    ctxSnow.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctxSnow.fillStyle = gradient;
    ctxSnow.shadowColor = "rgba(173, 216, 230, 0.8)";
    ctxSnow.shadowBlur = 10;
    ctxSnow.fill();
    ctxSnow.shadowBlur = 0;
  }
}

function initSnow() {
  snowflakes = [];
  for (let i = 0; i < 150; i++) {
    snowflakes.push(new Snowflake());
  }
}
initSnow();

function animateSnow() {
  ctxSnow.clearRect(0, 0, snowCanvas.width, snowCanvas.height);
  snowflakes.forEach(flake => {
    flake.update();
    flake.draw();
  });
  requestAnimationFrame(animateSnow);
}
animateSnow();

window.addEventListener("resize", () => {
  snowCanvas.width = window.innerWidth;
  snowCanvas.height = window.innerHeight;
  initSnow();
});


// ==================== 📘 Sidebar Menu ====================
const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebar");
const hamburgerIcon = hamburger.querySelector("span");

function toggleSidebar() {
  const isOpen = sidebar.classList.toggle("open");
  hamburger.setAttribute("aria-expanded", isOpen ? "true" : "false");
  hamburgerIcon.textContent = isOpen ? "✕" : "☰";
  document.body.classList.toggle("sidebar-open", isOpen);
}
hamburger.addEventListener("click", toggleSidebar);

document.addEventListener("click", (e) => {
  if (!sidebar.contains(e.target) && !hamburger.contains(e.target)) {
    sidebar.classList.remove("open");
    hamburger.setAttribute("aria-expanded", "false");
    hamburgerIcon.textContent = "☰";
    document.body.classList.remove("sidebar-open");
  }
});

document.querySelectorAll(".sidebar a").forEach(link => {
  link.addEventListener("click", () => {
    sidebar.classList.remove("open");
    hamburger.setAttribute("aria-expanded", "false");
    hamburgerIcon.textContent = "☰";
    document.body.classList.remove("sidebar-open");
  });
});

document.querySelectorAll(".dropdown-toggle").forEach(toggle => {
  toggle.addEventListener("click", e => {
    e.preventDefault();
    const parent = toggle.parentElement;
    parent.classList.toggle("open");
  });
});


// ==================== ✉️ Form Contact Kirim ke WhatsApp ====================
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const nama = document.querySelector('input[name="nama"]').value.trim();
  const email = document.querySelector('input[name="email"]').value.trim();
  const pesan = document.querySelector('textarea[name="pesan"]').value.trim();

  if (!nama || !email || !pesan) {
    alert("Mohon isi semua kolom terlebih dahulu!");
    return;
  }

  const nomorWA = "6281285554702"; 
  const teks = `Halo, saya *${nama}*!\n\nEmail: ${email}\nPesan:\n${pesan}`;
  const url = `https://wa.me/${nomorWA}?text=${encodeURIComponent(teks)}`;

  // Buka WhatsApp
  window.open(url, "_blank");

  // Tampilkan pesan sukses di bawah form
  const successMsg = document.createElement("p");
  successMsg.textContent = `Terima kasih, ${nama}! Pesanmu sudah terkirim 😊`;
  successMsg.style.color = "green";
  successMsg.style.textAlign = "center";
  successMsg.style.marginTop = "10px";
  successMsg.style.transition = "opacity 0.8s ease";

  const oldMsg = document.querySelector(".success-message");
  if (oldMsg) oldMsg.remove();

  successMsg.classList.add("success-message");
  document.getElementById("contactForm").insertAdjacentElement("afterend", successMsg);

  // Fade in effect
  setTimeout(() => (successMsg.style.opacity = 1), 50);

  // Hapus pesan setelah 5 detik
  setTimeout(() => {
    successMsg.style.opacity = 0;
    setTimeout(() => successMsg.remove(), 800);
  }, 5000);

  // Reset form
  e.target.reset();
});
