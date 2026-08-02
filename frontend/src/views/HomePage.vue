<template>
  <div class="homepage-wrapper">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg sticky-top custom-navbar">
      <div class="container">
        <RouterLink class="navbar-brand d-flex align-items-center gap-2 fw-bold fs-4" to="/home">
          <div class="brand-icon-box">
            <i class="bi bi-mortarboard-fill"></i>
          </div>
          <span class="brand-text">Placement Portal</span>
        </RouterLink>

        <button
          class="navbar-toggler border-0 shadow-none"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbar">
          <ul class="navbar-nav ms-auto align-items-lg-center gap-2">
            <li class="nav-item">
              <a class="nav-link custom-nav-link px-3" href="#features">Features</a>
            </li>

            <li class="nav-item">
              <a class="nav-link custom-nav-link px-3" href="#how">How It Works</a>
            </li>

            <li class="nav-item ms-lg-2">
              <RouterLink class="btn btn-outline-light nav-btn-login px-3 py-1-5" to="/login">
                Login
              </RouterLink>
            </li>

            <li class="nav-item d-flex gap-2 ms-lg-1">
              <RouterLink class="btn btn-warning nav-btn-student px-3 py-1-5" to="/student-register">
                Student
              </RouterLink>

              <RouterLink class="btn btn-emerald nav-btn-company px-3 py-1-5" to="/company-register">
                Company
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container position-relative z-1">
        <div class="row align-items-center gy-5">
          <div class="col-lg-6 text-lg-start text-center">
            <div class="badge-pill mb-3 d-inline-flex align-items-center gap-2">
              <span class="badge-dot"></span>
              <span>Next-Gen Placement Platform</span>
            </div>

            <h1 class="display-3 fw-extrabold hero-title mb-4">
              Find Your <span class="gradient-text">Dream Career</span>
            </h1>

            <p class="hero-subtitle mb-4">
              A complete placement portal connecting Students, Companies and Placement Cell through one modern platform.
            </p>

            <div class="d-flex flex-wrap align-items-center justify-content-lg-start justify-content-center gap-3">
              <RouterLink to="/login" class="btn btn-primary btn-lg shadow-sm px-4">
                Login
              </RouterLink>

              <RouterLink to="/student-register" class="btn btn-outline-primary btn-lg px-4">
                Student Register
              </RouterLink>

              <RouterLink to="/company-register" class="btn btn-success btn-lg shadow-sm px-4">
                Company Register
              </RouterLink>
            </div>
          </div>

          <div class="col-lg-6 text-center">
            <div class="hero-graphic-wrapper">
              <div class="hero-graphic-glow"></div>
              <div class="hero-icon-card">
                <i class="bi bi-briefcase-fill hero-icon"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="py-5 bg-white border-bottom border-top">
      <div class="container py-3">
        <div class="row text-center g-4">
          <div class="col-md-3 col-6">
            <div class="card stat-card border-0 h-100 p-4">
              <div class="stat-icon-box bg-primary-subtle text-primary mb-3 mx-auto">
                <i class="bi bi-people-fill"></i>
              </div>
              <h2 class="fw-bold text-dark mb-1">1000+</h2>
              <p class="text-secondary fw-medium mb-0">Students</p>
            </div>
          </div>

          <div class="col-md-3 col-6">
            <div class="card stat-card border-0 h-100 p-4">
              <div class="stat-icon-box bg-success-subtle text-success mb-3 mx-auto">
                <i class="bi bi-building"></i>
              </div>
              <h2 class="fw-bold text-dark mb-1">250+</h2>
              <p class="text-secondary fw-medium mb-0">Companies</p>
            </div>
          </div>

          <div class="col-md-3 col-6">
            <div class="card stat-card border-0 h-100 p-4">
              <div class="stat-icon-box bg-warning-subtle text-warning mb-3 mx-auto">
                <i class="bi bi-briefcase-fill"></i>
              </div>
              <h2 class="fw-bold text-dark mb-1">500+</h2>
              <p class="text-secondary fw-medium mb-0">Placement Drives</p>
            </div>
          </div>

          <div class="col-md-3 col-6">
            <div class="card stat-card border-0 h-100 p-4">
              <div class="stat-icon-box bg-danger-subtle text-danger mb-3 mx-auto">
                <i class="bi bi-check-circle-fill"></i>
              </div>
              <h2 class="fw-bold text-dark mb-1">800+</h2>
              <p class="text-secondary fw-medium mb-0">Applications</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-5 bg-slate-50">
      <div class="container py-4">
        <div class="text-center mb-5">
          <span class="text-primary fw-semibold text-uppercase tracking-wider fs-7">Role Based Workflows</span>
          <h2 class="fw-extrabold text-dark mt-1">Everything You Need for Placements</h2>
          <p class="text-muted">One platform for Students, Companies and Placement Cell.</p>
        </div>

        <div class="row g-4">
          <!-- Student Role -->
          <div class="col-lg-4">
            <div class="card feature-card h-100 border-0 shadow-sm">
              <div class="card-body p-4">
                <div class="text-center mb-4">
                  <div class="feature-badge bg-primary-subtle text-primary mb-3 mx-auto">
                    <i class="bi bi-person-workspace feature-icon"></i>
                  </div>
                  <h3 class="h4 fw-bold text-dark">Student</h3>
                </div>

                <ul class="list-group list-group-flush custom-feature-list">
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Update Profile</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Upload Resume</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Search Placement Drives</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Apply for Jobs</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Track Applications</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Interview Schedule</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Company Role -->
          <div class="col-lg-4">
            <div class="card feature-card h-100 border-0 shadow-sm">
              <div class="card-body p-4">
                <div class="text-center mb-4">
                  <div class="feature-badge bg-success-subtle text-success mb-3 mx-auto">
                    <i class="bi bi-building feature-icon"></i>
                  </div>
                  <h3 class="h4 fw-bold text-dark">Company</h3>
                </div>

                <ul class="list-group list-group-flush custom-feature-list">
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Create Placement Drives</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Manage Applicants</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Shortlist Students</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Schedule Interviews</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Final Selection</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Close / Reopen Drives</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Admin Role -->
          <div class="col-lg-4">
            <div class="card feature-card h-100 border-0 shadow-sm">
              <div class="card-body p-4">
                <div class="text-center mb-4">
                  <div class="feature-badge bg-danger-subtle text-danger mb-3 mx-auto">
                    <i class="bi bi-shield-lock feature-icon"></i>
                  </div>
                  <h3 class="h4 fw-bold text-dark">Admin</h3>
                </div>

                <ul class="list-group list-group-flush custom-feature-list">
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Dashboard Analytics</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Approve Companies</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Approve Drives</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Manage Students</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Manage Companies</li>
                  <li class="list-group-item"><i class="bi bi-check-circle-fill text-success me-2"></i> Blacklist Users</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section id="how" class="py-5 bg-white">
      <div class="container py-4">
        <div class="text-center mb-5">
          <span class="text-primary fw-semibold text-uppercase tracking-wider fs-7">End-to-End Workflow</span>
          <h2 class="fw-extrabold text-dark mt-1">How It Works</h2>
          <p class="text-muted">Placement process made simple in six easy steps.</p>
        </div>

        <div class="row text-center g-4">
          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-primary">
                <i class="bi bi-person-plus-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Register</h5>
              <p class="text-muted small mb-0">Student or Company creates an account.</p>
            </div>
          </div>

          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-success">
                <i class="bi bi-briefcase-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Create Drive</h5>
              <p class="text-muted small mb-0">Company posts placement opportunities.</p>
            </div>
          </div>

          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-warning">
                <i class="bi bi-file-earmark-check-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Apply</h5>
              <p class="text-muted small mb-0">Eligible students submit applications.</p>
            </div>
          </div>

          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-info">
                <i class="bi bi-person-check-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Shortlist</h5>
              <p class="text-muted small mb-0">Company reviews and shortlists candidates.</p>
            </div>
          </div>

          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-danger">
                <i class="bi bi-calendar-event-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Interview</h5>
              <p class="text-muted small mb-0">Interview schedule is shared with students.</p>
            </div>
          </div>

          <div class="col-lg-2 col-md-4 col-6">
            <div class="step-card h-100">
              <div class="step-circle step-circle-dark">
                <i class="bi bi-trophy-fill"></i>
              </div>
              <h5 class="fw-bold fs-6 mt-3 mb-1">Selected</h5>
              <p class="text-muted small mb-0">Final selection and placement completed.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tech Stack Section -->
    <section class="py-5 bg-slate-50 border-top">
      <div class="container py-4">
        <div class="text-center mb-5">
          <span class="text-primary fw-semibold text-uppercase tracking-wider fs-7">Robust Architecture</span>
          <h2 class="fw-extrabold text-dark mt-1">Built With Modern Technologies</h2>
          <p class="text-muted">The Placement Portal is developed using industry-standard technologies.</p>
        </div>

        <div class="row text-center g-4">
          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-filetype-vue text-success"></i>
              <h6 class="fw-bold mt-3 mb-0">Vue 3</h6>
            </div>
          </div>

          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-server text-primary"></i>
              <h6 class="fw-bold mt-3 mb-0">Flask</h6>
            </div>
          </div>

          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-database-fill text-warning"></i>
              <h6 class="fw-bold mt-3 mb-0">SQLite</h6>
            </div>
          </div>

          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-bootstrap-fill text-purple"></i>
              <h6 class="fw-bold mt-3 mb-0">Bootstrap</h6>
            </div>
          </div>

          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-lightning-charge-fill text-danger"></i>
              <h6 class="fw-bold mt-3 mb-0">Redis</h6>
            </div>
          </div>

          <div class="col-md-2 col-4">
            <div class="tech-card border-0 shadow-sm h-100">
              <i class="bi bi-clock-history text-dark"></i>
              <h6 class="fw-bold mt-3 mb-0">Celery</h6>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="custom-footer text-white pt-5 pb-4">
      <div class="container">
        <div class="row gy-4 mb-4">
          <div class="col-md-4">
            <h4 class="fw-bold d-flex align-items-center gap-2 mb-3">
              <i class="bi bi-mortarboard-fill text-primary"></i>
              <span>Placement Portal</span>
            </h4>
            <p class="text-secondary small leading-relaxed">
              Connecting talented students with leading companies through one modern placement platform.
            </p>
          </div>

          <div class="col-md-4">
            <h6 class="fw-bold text-uppercase tracking-wider text-light mb-3">Quick Links</h6>
            <ul class="list-unstyled d-flex flex-column gap-2 mb-0">
              <li>
                <a href="#features" class="footer-link">
                  <i class="bi bi-chevron-right fs-8 me-1"></i> Features
                </a>
              </li>
              <li>
                <a href="#how" class="footer-link">
                  <i class="bi bi-chevron-right fs-8 me-1"></i> How It Works
                </a>
              </li>
              <li>
                <RouterLink to="/login" class="footer-link">
                  <i class="bi bi-chevron-right fs-8 me-1"></i> Login
                </RouterLink>
              </li>
              <li>
                <RouterLink to="/register" class="footer-link">
                  <i class="bi bi-chevron-right fs-8 me-1"></i> Register
                </RouterLink>
              </li>
            </ul>
          </div>

          <div class="col-md-4">
            <h6 class="fw-bold text-uppercase tracking-wider text-light mb-3">Project Information</h6>
            <p class="text-secondary small mb-1">IIT Madras BS Degree</p>
            <p class="text-secondary small">Modern Application Development II</p>
          </div>
        </div>

        <hr class="border-secondary opacity-25 my-4">

        <div class="text-center text-secondary small">
          © 2026 Placement Portal | All Rights Reserved
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* Core Typography & Variables */
.homepage-wrapper {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1e293b;
  background-color: #f8fafc;
}

.fs-7 { font-size: 0.8125rem; }
.fs-8 { font-size: 0.75rem; }
.tracking-wider { letter-spacing: 0.08em; }
.fw-extrabold { font-weight: 800; }
.bg-slate-50 { background-color: #f8fafc; }

/* Custom Navbar */
.custom-navbar {
  background-color: #0f172a !important;
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.brand-icon-box {
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.brand-text {
  color: #ffffff;
  letter-spacing: -0.02em;
}

.custom-nav-link {
  color: #94a3b8 !important;
  font-weight: 500;
  transition: all 0.2s ease;
}

.custom-nav-link:hover {
  color: #ffffff !important;
}

.nav-btn-login {
  border-color: rgba(255, 255, 255, 0.2);
  color: #f8fafc;
  font-weight: 500;
}

.nav-btn-login:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.4);
  color: #ffffff;
}

.btn-emerald {
  background-color: #10b981;
  color: #ffffff;
  border: none;
  font-weight: 500;
}
.btn-emerald:hover {
  background-color: #059669;
  color: #ffffff;
}

/* Hero Section */
.hero-section {
  min-height: 85vh;
  display: flex;
  align-items: center;
  position: relative;
  background: radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.08) 0%, rgba(255, 255, 255, 0) 60%),
              radial-gradient(circle at 90% 80%, rgba(16, 185, 129, 0.06) 0%, rgba(255, 255, 255, 0) 60%),
              #ffffff;
  padding: 4rem 0;
  overflow: hidden;
}

.badge-pill {
  background-color: #eff6ff;
  border: 1px solid #dbeafe;
  color: #1d4ed8;
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  font-size: 0.85rem;
  font-weight: 600;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background-color: #2563eb;
  border-radius: 50%;
}

.hero-title {
  color: #0f172a;
  letter-spacing: -0.03em;
  line-height: 1.15;
}

.gradient-text {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.15rem;
  color: #64748b;
  max-width: 520px;
  line-height: 1.6;
}

.hero-graphic-wrapper {
  position: relative;
  display: inline-block;
}

.hero-graphic-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 280px;
  height: 280px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.25), rgba(16, 185, 129, 0.2));
  filter: blur(50px);
  border-radius: 50%;
  z-index: 0;
}

.hero-icon-card {
  position: relative;
  z-index: 1;
  width: 240px;
  height: 240px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  box-shadow: 0 20px 40px -15px rgba(15, 23, 42, 0.1);
}

.hero-icon {
  font-size: 110px;
  background: linear-gradient(135deg, #2563eb, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Stats Cards */
.stat-card {
  border-radius: 16px;
  background: #ffffff;
  border: 1px solid #f1f5f9 !important;
  transition: all 0.25s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -10px rgba(15, 23, 42, 0.08) !important;
}

.stat-icon-box {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

/* Feature Cards */
.feature-card {
  border-radius: 20px;
  background: #ffffff;
  border: 1px solid #e2e8f0 !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 30px -10px rgba(15, 23, 42, 0.08) !important;
}

.feature-badge {
  width: 72px;
  height: 72px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-icon {
  font-size: 2.25rem;
}

.custom-feature-list .list-group-item {
  border: none;
  padding: 0.65rem 0;
  background: transparent;
  color: #475569;
  font-size: 0.95rem;
  font-weight: 500;
}

/* How It Works Steps */
.step-card {
  padding: 1rem 0.5rem;
  transition: transform 0.25s ease;
}

.step-card:hover {
  transform: translateY(-4px);
}

.step-circle {
  width: 68px;
  height: 68px;
  border-radius: 18px;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-size: 1.65rem;
  box-shadow: 0 8px 16px -4px rgba(0, 0, 0, 0.12);
  transition: transform 0.25s ease;
}

.step-card:hover .step-circle {
  transform: scale(1.08);
}

.step-circle-primary { background: linear-gradient(135deg, #3b82f6, #2563eb); }
.step-circle-success { background: linear-gradient(135deg, #10b981, #059669); }
.step-circle-warning { background: linear-gradient(135deg, #f59e0b, #d97706); }
.step-circle-info { background: linear-gradient(135deg, #06b6d4, #0891b2); }
.step-circle-danger { background: linear-gradient(135deg, #ef4444, #dc2626); }
.step-circle-dark { background: linear-gradient(135deg, #334155, #0f172a); }

/* Tech Stack Cards */
.tech-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 1.5rem 1rem;
  border: 1px solid #f1f5f9 !important;
  transition: all 0.25s ease;
}

.tech-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 20px -8px rgba(15, 23, 42, 0.08) !important;
}

.tech-card i {
  font-size: 2.75rem;
}

.text-purple { color: #8b5cf6; }

/* Buttons & Footer */
.btn {
  border-radius: 10px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.custom-footer {
  background-color: #0f172a;
}

.footer-link {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: #38bdf8;
}

html {
  scroll-behavior: smooth;
}

section {
  scroll-margin-top: 80px;
}
</style>