<template>
  <div class="admin-dashboard-wrapper bg-slate-50 min-vh-100 pb-5">
    
    <!-- Top Navigation Header -->
    <header class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top shadow-sm py-2">
      <div class="container-fluid px-4">
        <div class="d-flex align-items-center gap-2">
          <div class="brand-icon-box bg-primary text-white rounded-3 d-flex align-items-center justify-content-center p-2">
            <i class="bi bi-shield-lock-fill fs-5"></i>
          </div>
          <div>
            <h5 class="fw-bold text-white mb-0">Placement Portal</h5>
            <span class="badge bg-danger-subtle text-danger border border-danger-subtle fs-8">Admin Console</span>
          </div>
        </div>

        <button
          class="btn btn-outline-danger btn-sm px-3 rounded-pill"
          @click="logout"
        >
          <i class="bi bi-box-arrow-right me-1"></i> Logout
        </button>
      </div>
    </header>

    <div class="container-fluid px-4 mt-4">

      <!-- Alert Notification -->
      <div
        v-if="successMessage"
        class="alert alert-success alert-dismissible fade show border-0 shadow-sm rounded-3 mb-4 d-flex align-items-center gap-2"
        role="alert"
      >
        <i class="bi bi-check-circle-fill fs-5 text-success"></i>
        <div>{{ successMessage }}</div>
      </div>

      <!-- Stat Cards Grid -->
      <div class="row g-3 mb-4">
        <div class="col-12 col-sm-6 col-xl-3">
          <div class="card border-0 shadow-sm rounded-3 h-100 card-hover">
            <div class="card-body p-4 d-flex align-items-center justify-content-between">
              <div>
                <p class="text-secondary small fw-semibold text-uppercase tracking-wider mb-1">Students</p>
                <h2 class="fw-bold text-dark mb-0">{{ dashboard.total_students || 0 }}</h2>
              </div>
              <div class="stat-icon-box bg-primary-subtle text-primary rounded-3">
                <i class="bi bi-people-fill fs-3"></i>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-xl-3">
          <div class="card border-0 shadow-sm rounded-3 h-100 card-hover">
            <div class="card-body p-4 d-flex align-items-center justify-content-between">
              <div>
                <p class="text-secondary small fw-semibold text-uppercase tracking-wider mb-1">Companies</p>
                <h2 class="fw-bold text-dark mb-0">{{ dashboard.total_companies || 0 }}</h2>
              </div>
              <div class="stat-icon-box bg-success-subtle text-success rounded-3">
                <i class="bi bi-building fs-3"></i>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-xl-3">
          <div class="card border-0 shadow-sm rounded-3 h-100 card-hover">
            <div class="card-body p-4 d-flex align-items-center justify-content-between">
              <div>
                <p class="text-secondary small fw-semibold text-uppercase tracking-wider mb-1">Drives</p>
                <h2 class="fw-bold text-dark mb-0">{{ dashboard.total_drives || 0 }}</h2>
              </div>
              <div class="stat-icon-box bg-warning-subtle text-warning rounded-3">
                <i class="bi bi-briefcase-fill fs-3"></i>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-xl-3">
          <div class="card border-0 shadow-sm rounded-3 h-100 card-hover">
            <div class="card-body p-4 d-flex align-items-center justify-content-between">
              <div>
                <p class="text-secondary small fw-semibold text-uppercase tracking-wider mb-1">Applications</p>
                <h2 class="fw-bold text-dark mb-0">{{ dashboard.total_applications || 0 }}</h2>
              </div>
              <div class="stat-icon-box bg-info-subtle text-info rounded-3">
                <i class="bi bi-file-earmark-check-fill fs-3"></i>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Toolbar -->
      <div class="card border-0 shadow-sm rounded-3 mb-5">
        <div class="card-body p-3">
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-2">
            <div class="fw-semibold text-dark small d-flex align-items-center gap-2">
              <i class="bi bi-sliders text-primary"></i> System Actions & Reports
            </div>
            <div class="d-flex flex-wrap gap-2">
              <button
                class="btn btn-success btn-sm px-3 fw-medium rounded-2"
                @click="exportStudents"
                :disabled="exporting"
              >
                <i class="bi bi-file-earmark-spreadsheet me-1"></i>
                {{ exporting ? "Generating CSV..." : "Export Students" }}
              </button>

              <button
                class="btn btn-primary btn-sm px-3 fw-medium rounded-2"
                @click="downloadStudents"
                :disabled="!exportCompleted"
              >
                <i class="bi bi-download me-1"></i> Download Latest CSV
              </button>

              <button
                class="btn btn-warning btn-sm px-3 fw-medium rounded-2"
                @click="runDailyReminder"
              >
                <i class="bi bi-bell me-1"></i> Run Daily Reminder
              </button>

              <button
                class="btn btn-dark btn-sm px-3 fw-medium rounded-2"
                @click="runMonthlyReport"
              >
                <i class="bi bi-bar-chart me-1"></i> Run Monthly Report
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Company Management Section -->
      <div class="card border-0 shadow-sm rounded-3 mb-5">
        <div class="card-header bg-white py-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div class="d-flex align-items-center gap-2">
            <div class="icon-square bg-success-subtle text-success rounded-2 p-2">
              <i class="bi bi-building"></i>
            </div>
            <h5 class="fw-bold text-dark mb-0">Company Management</h5>
          </div>

          <div class="input-group" style="max-width: 360px;">
            <span class="input-group-text bg-light border-end-0 text-muted">
              <i class="bi bi-search"></i>
            </span>
            <input
              v-model="companySearch"
              @input="loadCompanies"
              type="text"
              class="form-control bg-light border-start-0 ps-0"
              placeholder="Search by company, industry or HR name..."
            />
          </div>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Company</th>
                <th>Industry</th>
                <th>HR Name</th>
                <th>Approval Status</th>
                <th>Account Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="company in companies" :key="company.id">
                <td class="ps-4 fw-semibold text-dark">{{ company.company_name }}</td>
                <td><span class="badge bg-light text-dark border">{{ company.industry }}</span></td>
                <td>{{ company.hr_name }}</td>
                <td>
                  <div class="d-flex align-items-center gap-2">
                    <span
                      class="badge rounded-pill px-2-5 py-1"
                      :class="{
                        'bg-success-subtle text-success border border-success-subtle': company.approval_status === 'Approved',
                        'bg-warning-subtle text-warning border border-warning-subtle': company.approval_status === 'Pending',
                        'bg-danger-subtle text-danger border border-danger-subtle': company.approval_status === 'Rejected'
                      }"
                    >
                      {{ company.approval_status }}
                    </span>

                    <button
                      class="btn btn-outline-success btn-xs px-2 py-0-5"
                      @click="approveCompany(company.id)"
                    >
                      Approve
                    </button>

                    <button
                      class="btn btn-outline-danger btn-xs px-2 py-0-5"
                      @click="rejectCompany(company.id)"
                    >
                      Reject
                    </button>
                  </div>
                </td>
                <td>
                  <div class="d-flex align-items-center gap-2">
                    <span
                      class="badge rounded-pill px-2-5 py-1"
                      :class="company.is_active ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-danger-subtle text-danger border border-danger-subtle'"
                    >
                      {{ company.is_active ? "Active" : "Blacklisted" }}
                    </span>

                    <button
                      class="btn btn-outline-secondary btn-xs px-2 py-0-5"
                      @click="toggleCompanyStatus(company.id)"
                    >
                      {{ company.is_active ? "Blacklist" : "Activate" }}
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="companies.length === 0">
                <td colspan="5" class="text-center py-4 text-muted">No companies found</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Student Management Section -->
      <div class="card border-0 shadow-sm rounded-3 mb-5">
        <div class="card-header bg-white py-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div class="d-flex align-items-center gap-2">
            <div class="icon-square bg-primary-subtle text-primary rounded-2 p-2">
              <i class="bi bi-people"></i>
            </div>
            <h5 class="fw-bold text-dark mb-0">Student Management</h5>
          </div>

          <div class="input-group" style="max-width: 360px;">
            <span class="input-group-text bg-light border-end-0 text-muted">
              <i class="bi bi-search"></i>
            </span>
            <input
              v-model="studentSearch"
              @input="loadStudents"
              type="text"
              class="form-control bg-light border-start-0 ps-0"
              placeholder="Search by name, branch or phone..."
            />
          </div>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Name</th>
                <th>Branch</th>
                <th>CGPA</th>
                <th>Passing Year</th>
                <th>Skills</th>
                <th>Resume</th>
                <th>Account</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="student in students" :key="student.id">
                <td class="ps-4 fw-semibold text-dark">{{ student.full_name }}</td>
                <td><span class="badge bg-light text-dark border">{{ student.branch }}</span></td>
                <td class="fw-bold text-primary">{{ student.cgpa }}</td>
                <td>{{ student.passing_year }}</td>
                <td><small class="text-muted">{{ student.skills }}</small></td>
                <td>
                  <button
                    v-if="student.resume"
                    class="btn btn-outline-info btn-xs px-2 py-1"
                    @click="viewResume(student.id)"
                  >
                    <i class="bi bi-file-earmark-pdf me-1"></i> View Resume
                  </button>
                  <span v-else class="badge bg-light text-muted border">Not Uploaded</span>
                </td>
                <td>
                  <div class="d-flex align-items-center gap-2">
                    <span
                      class="badge rounded-pill px-2-5 py-1"
                      :class="student.is_active ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-danger-subtle text-danger border border-danger-subtle'"
                    >
                      {{ student.is_active ? "Active" : "Blacklisted" }}
                    </span>

                    <button
                      class="btn btn-outline-secondary btn-xs px-2 py-0-5"
                      @click="toggleStudentStatus(student.id)"
                    >
                      {{ student.is_active ? "Blacklist" : "Activate" }}
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="students.length === 0">
                <td colspan="7" class="text-center py-4 text-muted">No students found</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Placement Drives Section -->
      <div class="card border-0 shadow-sm rounded-3 mb-5">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-warning-subtle text-warning rounded-2 p-2">
            <i class="bi bi-briefcase"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">Placement Drives</h5>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Company</th>
                <th>Job Title</th>
                <th>Salary</th>
                <th>Deadline</th>
                <th>Drive Status</th>
                <th>Approval</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="drive in drives" :key="drive.id">
                <td class="ps-4 fw-semibold text-dark">{{ drive.company_name }}</td>
                <td>{{ drive.job_title }}</td>
                <td class="fw-medium text-success">{{ drive.salary }}</td>
                <td><small class="text-muted">{{ drive.application_deadline }}</small></td>
                <td>
                  <span
                    class="badge rounded-pill px-2-5 py-1"
                    :class="drive.status === 'Open' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-danger-subtle text-danger border border-danger-subtle'"
                  >
                    {{ drive.status }}
                  </span>
                </td>
                <td>
                  <span
                    class="badge rounded-pill px-2-5 py-1"
                    :class="{
                      'bg-success-subtle text-success border border-success-subtle': drive.approval_status === 'Approved',
                      'bg-danger-subtle text-danger border border-danger-subtle': drive.approval_status === 'Rejected',
                      'bg-warning-subtle text-warning border border-warning-subtle': drive.approval_status === 'Pending'
                    }"
                  >
                    {{ drive.approval_status }}
                  </span>
                </td>
                <td>
                  <div class="d-flex align-items-center gap-2">
                    <button
                      class="btn btn-outline-success btn-xs px-2 py-0-5"
                      @click="approveDrive(drive.id)"
                      :disabled="drive.approval_status === 'Approved'"
                    >
                      Approve
                    </button>

                    <button
                      class="btn btn-outline-danger btn-xs px-2 py-0-5"
                      @click="rejectDrive(drive.id)"
                      :disabled="drive.approval_status === 'Rejected'"
                    >
                      Reject
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="drives.length === 0">
                <td colspan="7" class="text-center py-4 text-muted">No placement drives found</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Student Applications Section -->
      <div class="card border-0 shadow-sm rounded-3">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-info-subtle text-info rounded-2 p-2">
            <i class="bi bi-file-earmark-check"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">Student Applications</h5>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Student</th>
                <th>Company</th>
                <th>Job Title</th>
                <th>Status</th>
                <th>Applied On</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="application in applications" :key="application.id">
                <td class="ps-4 fw-semibold text-dark">{{ application.student_name }}</td>
                <td>{{ application.company_name }}</td>
                <td>{{ application.job_title }}</td>
                <td>
                  <span
                    class="badge rounded-pill px-2-5 py-1"
                    :class="{
                      'bg-primary-subtle text-primary border border-primary-subtle': application.status === 'Applied',
                      'bg-warning-subtle text-warning border border-warning-subtle': application.status === 'Shortlisted',
                      'bg-success-subtle text-success border border-success-subtle': application.status === 'Selected',
                      'bg-danger-subtle text-danger border border-danger-subtle': application.status === 'Rejected'
                    }"
                  >
                    {{ application.status }}
                  </span>
                </td>
                <td><small class="text-muted">{{ application.application_date }}</small></td>
              </tr>
              <tr v-if="applications.length === 0">
                <td colspan="5" class="text-center py-4 text-muted">No student applications found</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";
import { useRouter } from "vue-router";

const router = useRouter();
const dashboard = ref({});
const companies = ref([]);
const students = ref([]);
const drives = ref([]);
const applications = ref([]);
const applicationSearch = ref("");
const studentSearch = ref("");
const companySearch = ref("");
const exporting = ref(false);
const successMessage = ref("");
const exportCompleted = ref(false);

async function loadDashboard() {
  try {
    const response = await api.get("/admin/dashboard");
    console.log("Dashboard data:", response.data);
    dashboard.value = response.data;
  } catch (error) {
    alert(error.response?.data?.message || "Failed to load dashboard");
  }
}

async function loadCompanies() {
  try {
    const response = await api.get("/admin/companies", {
      params: {
        search: companySearch.value
      }
    });

    companies.value = response.data;
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load companies."
    );
  }
}

async function loadStudents() {
  try {
    const response = await api.get("/admin/students", {
      params: {
        search: studentSearch.value
      }
    });

    students.value = response.data;
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load students."
    );
  }
}

async function approveCompany(id) {
  try {
    await api.put(`/admin/company/${id}/approve`);
    loadCompanies();
    loadDashboard();
  } catch (error) {
    alert(error.response?.data?.message || "Approval failed");
  }
}

async function rejectCompany(id) {
  try {
    await api.put(`/admin/company/${id}/reject`);
    loadCompanies();
    loadDashboard();
  } catch (error) {
    alert(error.response?.data?.message || "Reject failed");
  }
}

async function toggleCompanyStatus(id) {
  try {
    const response = await api.put(
      `/admin/company/${id}/toggle-status`
    );

    successMessage.value = response.data.message;
    loadCompanies();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to update company status."
    );
  }
}

async function toggleStudentStatus(id) {
  try {
    const response = await api.put(
      `/admin/student/${id}/toggle-status`
    );

    successMessage.value = response.data.message;
    loadStudents();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to update student status."
    );
  }
}

const loadDrives = async () => {
  try {
    const response = await api.get("/admin/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

async function loadApplications() {
  try {
    const response = await api.get("/admin/applications");
    applications.value = response.data;
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load applications."
    );
  }
}

const approveDrive = async (id) => {
  try {
    await api.put(`/admin/drive/${id}/approve`);
    alert("Drive approved successfully!");
    await loadDrives();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to approve drive."
    );
  }
};

const rejectDrive = async (id) => {
  try {
    await api.put(`/admin/drive/${id}/reject`);
    alert("Drive rejected successfully!");
    await loadDrives();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to reject drive."
    );
  }
};

async function logout() {
  try {
    const response = await api.post("/logout");
    alert(response.data.message);
    router.push("/login");
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Logout failed."
    );
  }
}

function viewResume(studentId) {
  window.open(
    `http://localhost:5000/api/admin/resume/${studentId}`,
    "_blank"
  );
}

async function exportStudents() {
  try {
    exporting.value = true;
    const response = await api.post("/admin/export-students");

    successMessage.value = response.data.message;
    exportCompleted.value = true;

    setTimeout(() => {
      successMessage.value = "";
    }, 3000);
  } catch (error) {
    console.error(error);
    successMessage.value = "Export failed!";
  } finally {
    exporting.value = false;
  }
}

async function downloadStudents() {
  try {
    window.open(
      "http://127.0.0.1:5000/api/admin/download-students",
      "_blank"
    );
  } catch (error) {
    console.error(error);
    alert("Download failed!");
  }
}

async function runDailyReminder() {
  try {
    const response = await api.post("/admin/daily-reminder");
    successMessage.value = response.data.message;

    setTimeout(() => {
      successMessage.value = "";
    }, 3000);
  } catch (error) {
    console.error(error);
    successMessage.value = "Failed to start reminder!";
  }
}

async function runMonthlyReport() {
  try {
    const response = await api.post(
      "/admin/monthly-report"
    );

    successMessage.value = response.data.message;

    setTimeout(() => {
      successMessage.value = "";
    }, 3000);
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Monthly report failed."
    );
  }
}

onMounted(() => {
  loadDashboard();
  loadCompanies();
  loadStudents();
  loadDrives();
  loadApplications();
});
</script>

<style scoped>
.admin-dashboard-wrapper {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1e293b;
}

.bg-slate-50 {
  background-color: #f8fafc;
}

.brand-icon-box {
  width: 36px;
  height: 36px;
}

.stat-icon-box {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-square {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-hover {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card-hover:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -5px rgba(15, 23, 42, 0.08) !important;
}

.table th {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #64748b;
  font-weight: 700;
  border-bottom: 1px solid #e2e8f0;
}

.table td {
  font-size: 0.9rem;
  border-bottom: 1px solid #f1f5f9;
}

.btn-xs {
  font-size: 0.75rem;
  border-radius: 0.375rem;
}

.px-2-5 {
  padding-left: 0.625rem;
  padding-right: 0.625rem;
}

.py-0-5 {
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}

.fs-8 {
  font-size: 0.7rem;
}

.tracking-wider {
  letter-spacing: 0.05em;
}
</style>