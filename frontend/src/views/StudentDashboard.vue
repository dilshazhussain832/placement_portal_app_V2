<template>
  <div class="student-dashboard-wrapper bg-slate-50 min-vh-100 pb-5">

    <!-- Top Navigation Header -->
    <header class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top shadow-sm py-2">
      <div class="container-fluid px-4">
        <div class="d-flex align-items-center gap-2">
          <div class="brand-icon-box bg-primary text-white rounded-3 d-flex align-items-center justify-content-center p-2">
            <i class="bi bi-mortarboard-fill fs-5"></i>
          </div>
          <div>
            <h5 class="fw-bold text-white mb-0">Placement Portal</h5>
            <span class="badge bg-primary-subtle text-primary border border-primary-subtle fs-8">Student Console</span>
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

      <!-- Profile & Resume Section -->
      <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-primary-subtle text-primary rounded-2 p-2">
            <i class="bi bi-person-badge"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">My Profile</h5>
        </div>

        <div class="card-body p-4">
          <div class="row g-3 mb-3">
            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Full Name</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-person"></i></span>
                <input
                  v-model="profile.full_name"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="John Doe"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Phone Number</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-telephone"></i></span>
                <input
                  v-model="profile.phone"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="+91 9876543210"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Branch</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-journal-bookmark"></i></span>
                <input
                  v-model="profile.branch"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="Computer Science"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-6">
              <label class="form-label fw-semibold text-secondary small">CGPA</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-award"></i></span>
                <input
                  v-model="profile.cgpa"
                  class="form-control bg-light border-start-0 ps-0"
                  type="number"
                  step="0.01"
                  placeholder="8.5"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-6">
              <label class="form-label fw-semibold text-secondary small">Passing Year</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-calendar-event"></i></span>
                <input
                  v-model="profile.passing_year"
                  class="form-control bg-light border-start-0 ps-0"
                  type="number"
                  placeholder="2026"
                />
              </div>
            </div>

            <div class="col-12">
              <label class="form-label fw-semibold text-secondary small">Technical Skills</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted align-items-start pt-2"><i class="bi bi-code-slash"></i></span>
                <textarea
                  v-model="profile.skills"
                  class="form-control bg-light border-start-0 ps-0"
                  rows="3"
                  placeholder="Python, SQL, Vue.js, Flask"
                ></textarea>
              </div>
            </div>
          </div>

          <!-- Resume Upload Block -->
          <div v-if="!resumeName || showUpload" class="card bg-light border-dashed p-3 mb-4 rounded-3">
            <div class="mb-3">
              <label class="form-label fw-semibold text-secondary small">Upload Resume (PDF)</label>
              <input
                type="file"
                class="form-control bg-white"
                accept=".pdf"
                @change="selectResume"
              >
            </div>

            <div>
              <button
                class="btn btn-success btn-sm px-3 fw-medium rounded-2"
                @click="uploadResume"
              >
                <i class="bi bi-cloud-upload me-1"></i> Upload Resume
              </button>
            </div>
          </div>

          <div
            v-else
            class="alert alert-success border-0 shadow-sm rounded-3 d-flex flex-wrap align-items-center justify-content-between p-3 mb-4 gap-2"
          >
            <div class="d-flex align-items-center gap-2">
              <i class="bi bi-file-earmark-check-fill fs-4 text-success"></i>
              <div>
                <strong class="d-block text-dark">Resume Uploaded:</strong>
                <span class="text-secondary small">{{ resumeName }}</span>
              </div>
            </div>

            <div class="d-flex gap-2">
              <button
                class="btn btn-outline-primary btn-sm px-3 rounded-2"
                @click="viewResume"
              >
                <i class="bi bi-eye me-1"></i> View Resume
              </button>

              <button
                class="btn btn-warning btn-sm px-3 rounded-2 text-dark"
                @click="showUpload = true"
              >
                <i class="bi bi-arrow-repeat me-1"></i> Replace Resume
              </button>
            </div>
          </div>

          <button
            class="btn btn-primary px-4 fw-medium rounded-2"
            @click="updateProfile"
          >
            <i class="bi bi-check-circle me-1"></i> Update Profile
          </button>
        </div>
      </div>

      <!-- Available Placement Drives Section -->
      <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-header bg-white py-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div class="d-flex align-items-center gap-2">
            <div class="icon-square bg-warning-subtle text-warning rounded-2 p-2">
              <i class="bi bi-briefcase"></i>
            </div>
            <h5 class="fw-bold text-dark mb-0">Available Placement Drives</h5>
          </div>

          <div class="input-group" style="max-width: 360px;">
            <span class="input-group-text bg-light border-end-0 text-muted">
              <i class="bi bi-search"></i>
            </span>
            <input
              v-model="driveSearch"
              type="text"
              class="form-control bg-light border-start-0 ps-0"
              placeholder="Search by company, job title or eligibility..."
            />
          </div>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Company</th>
                <th>Job Title</th>
                <th>Eligibility</th>
                <th>Salary</th>
                <th>Deadline</th>
                <th class="pe-4 text-end">Action</th>
              </tr>
            </thead>

            <tbody>
              <tr v-if="filteredDrives.length === 0">
                <td colspan="100" class="text-center text-muted py-4">
                  No placement drives are available at the moment.
                </td>
              </tr>

              <tr
                v-for="drive in filteredDrives"
                :key="drive.id"
              >
                <td class="ps-4 fw-semibold text-dark">{{ drive.company_name }}</td>
                <td>{{ drive.job_title }}</td>
                <td><small class="text-muted">{{ drive.eligibility }}</small></td>
                <td class="fw-medium text-success">{{ drive.salary }}</td>
                <td><small class="text-muted">{{ drive.application_deadline }}</small></td>
                <td class="pe-4 text-end">
                  <button
                    v-if="!hasApplied(drive.id)"
                    class="btn btn-primary btn-sm px-3 rounded-2 shadow-sm"
                    @click="applyForDrive(drive.id)"
                  >
                    Apply Now
                  </button>

                  <button
                    v-else
                    class="btn btn-success btn-sm px-3 rounded-2"
                    disabled
                  >
                    <i class="bi bi-check2 me-1"></i> Applied
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- My Applications Section -->
      <div class="card border-0 shadow-sm rounded-3">
        <div class="card-header bg-white py-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div class="d-flex align-items-center gap-2">
            <div class="icon-square bg-info-subtle text-info rounded-2 p-2">
              <i class="bi bi-file-earmark-check"></i>
            </div>
            <h5 class="fw-bold text-dark mb-0">My Applications</h5>
          </div>

          <div class="d-flex gap-2">
            <button
              class="btn btn-success btn-sm px-3 fw-medium rounded-2"
              @click="exportApplications"
              :disabled="exporting"
            >
              <i class="bi bi-file-earmark-spreadsheet me-1"></i>
              {{ exporting ? "Generating CSV..." : "Export My Applications" }}
            </button>

            <button
              class="btn btn-primary btn-sm px-3 fw-medium rounded-2"
              @click="downloadApplications"
              :disabled="!exportCompleted"
            >
              <i class="bi bi-download me-1"></i> Download CSV
            </button>
          </div>
        </div>

        <div class="card-body p-0">
          <div
            v-if="successMessage"
            class="alert alert-success border-0 rounded-0 mb-0 d-flex align-items-center gap-2 p-3"
          >
            <i class="bi bi-check-circle-fill"></i>
            <span>{{ successMessage }}</span>
          </div>

          <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
              <thead class="bg-light">
                <tr>
                  <th class="ps-4">Company</th>
                  <th>Job Title</th>
                  <th>Applied On</th>
                  <th>Status</th>
                  <th>Interview Details</th>
                </tr>
              </thead>

              <tbody>
                <tr v-if="applications.length === 0">
                  <td colspan="100" class="text-center text-muted py-4">
                    You have not applied to any placement drives yet.
                  </td>
                </tr>

                <tr
                  v-for="application in applications"
                  :key="application.application_id"
                >
                  <td class="ps-4 fw-semibold text-dark">{{ application.company_name }}</td>
                  <td>{{ application.job_title }}</td>
                  <td><small class="text-muted">{{ application.application_date }}</small></td>
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
                  <td>
                    <div v-if="application.interview_date" class="small">
                      <div class="text-dark fw-semibold mb-1">
                        <i class="bi bi-calendar3 me-1 text-primary"></i> {{ application.interview_date }} at {{ application.interview_time }}
                      </div>
                      <div class="text-muted">
                        <span class="badge bg-light text-dark border me-1">{{ application.interview_mode }}</span>
                        <span>{{ application.interview_location }}</span>
                      </div>
                    </div>

                    <span
                      v-else
                      class="badge bg-light text-muted border fs-8"
                    >
                      Not Scheduled
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, reactive } from "vue";
import api from "../services/api";
import { useRouter } from "vue-router";

const router = useRouter();
const drives = ref([]);
const driveSearch = ref("");
const applications = ref([]);
const resumeFile = ref(null);
const resumeName = ref("");
const showUpload = ref(false);
const exporting = ref(false);
const exportCompleted = ref(false);
const successMessage = ref("");
const profile = reactive({
  full_name: "",
  phone: "",
  branch: "",
  cgpa: "",
  passing_year: "",
  skills: ""
});

const loadDrives = async () => {
  try {
    const response = await api.get("/student/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const loadApplications = async () => {
  try {
    const response = await api.get("/student/applications");
    applications.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const applyForDrive = async (driveId) => {
  try {
    const response = await api.post(`/student/apply/${driveId}`);

    alert(response.data.message);

    await loadDrives();
    await loadApplications();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to apply."
    );
  }
};

const hasApplied = (driveId) => {
  return applications.value.some(
    application => application.drive_id === driveId
  );
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

async function loadProfile() {
  try {
    const response = await api.get("/student/profile");

    Object.assign(profile, response.data);
    resumeName.value = response.data.resume || "";

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load profile."
    );
  }
}

async function updateProfile() {
  try {
    const response = await api.put(
      "/student/profile",
      profile
    );

    alert(response.data.message);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Profile update failed."
    );
  }
}

function selectResume(event) {
  resumeFile.value = event.target.files[0];
}

async function uploadResume() {
  if (!resumeFile.value) {
    alert("Please select a resume.");
    return;
  }

  const formData = new FormData();
  formData.append("resume", resumeFile.value);

  try {
    const response = await api.post(
      "/student/upload-resume",
      formData
    );

    resumeName.value = response.data.resume;
    resumeFile.value = null;
    showUpload.value = false;
    await loadProfile();

    alert(response.data.message);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Resume upload failed."
    );
  }
}

function viewResume() {
  window.open(
    "http://localhost:5000/api/student/resume",
    "_blank"
  );
}

async function exportApplications() {
  try {
    exporting.value = true;

    const response = await api.post(
      "/student/export-applications"
    );

    successMessage.value = response.data.message;
    exportCompleted.value = true;

    setTimeout(() => {
      successMessage.value = "";
    }, 3000);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Export failed."
    );
  } finally {
    exporting.value = false;
  }
}

async function downloadApplications() {
  try {
    const response = await api.get(
      "/student/download-applications",
      {
        responseType: "blob"
      }
    );

    const url = window.URL.createObjectURL(
      new Blob([response.data])
    );

    const link = document.createElement("a");
    link.href = url;
    link.setAttribute(
      "download",
      "my_applications.csv"
    );

    document.body.appendChild(link);
    link.click();
    link.remove();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Download failed."
    );
  }
}

const filteredDrives = computed(() => {
  const search = driveSearch.value.toLowerCase().trim();

  if (!search) {
    return drives.value;
  }

  return drives.value.filter(drive =>
    drive.company_name.toLowerCase().includes(search) ||
    drive.job_title.toLowerCase().includes(search) ||
    drive.eligibility.toLowerCase().includes(search)
  );
});

onMounted(() => {
  loadDrives();
  loadApplications();
  loadProfile();
});
</script>

<style scoped>
.student-dashboard-wrapper {
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

.icon-square {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.border-dashed {
  border: 2px dashed #cbd5e1 !important;
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
</style>