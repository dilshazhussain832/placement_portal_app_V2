<template>
  <div class="company-dashboard-wrapper bg-slate-50 min-vh-100 pb-5">

    <!-- Top Navigation Header -->
    <header class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top shadow-sm py-2">
      <div class="container-fluid px-4">
        <div class="d-flex align-items-center gap-2">
          <div class="brand-icon-box bg-emerald text-white rounded-3 d-flex align-items-center justify-content-center p-2">
            <i class="bi bi-building-fill fs-5"></i>
          </div>
          <div>
            <h5 class="fw-bold text-white mb-0">Placement Portal</h5>
            <span class="badge bg-success-subtle text-success border border-success-subtle fs-8">Company Console</span>
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

      <!-- Company Profile Card -->
      <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-emerald-subtle text-emerald rounded-2 p-2">
            <i class="bi bi-building-gear"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">My Company Profile</h5>
        </div>

        <div class="card-body p-4">
          <div class="row g-3 mb-3">
            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Company Name</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-building"></i></span>
                <input
                  v-model="companyProfile.company_name"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="Acme Corp"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Industry</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-briefcase"></i></span>
                <input
                  v-model="companyProfile.industry"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="Software & Tech"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-4">
              <label class="form-label fw-semibold text-secondary small">Website</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-globe"></i></span>
                <input
                  v-model="companyProfile.website"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="https://example.com"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-6">
              <label class="form-label fw-semibold text-secondary small">HR Name</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-person-badge"></i></span>
                <input
                  v-model="companyProfile.hr_name"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="Jane Smith"
                />
              </div>
            </div>

            <div class="col-md-6 col-lg-6">
              <label class="form-label fw-semibold text-secondary small">HR Contact Email</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-envelope-at"></i></span>
                <input
                  v-model="companyProfile.hr_email"
                  class="form-control bg-light border-start-0 ps-0"
                  placeholder="hr@example.com"
                />
              </div>
            </div>
          </div>

          <button
            class="btn btn-emerald px-4 fw-medium rounded-2"
            @click="updateCompanyProfile"
          >
            <i class="bi bi-check-circle me-1"></i> Update Profile
          </button>
        </div>
      </div>

      <!-- Create / Edit Placement Drive Card -->
      <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-primary-subtle text-primary rounded-2 p-2">
            <i class="bi bi-plus-circle"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">
            {{ editingDriveId === null ? "Create Placement Drive" : "Edit Placement Drive" }}
          </h5>
        </div>

        <div class="card-body p-4">
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <label class="form-label fw-semibold text-secondary small">Job Title</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-card-heading"></i></span>
                <input
                  class="form-control bg-light border-start-0 ps-0"
                  v-model="job_title"
                  placeholder="Software Development Engineer"
                />
              </div>
            </div>

            <div class="col-md-6">
              <label class="form-label fw-semibold text-secondary small">Salary / CTC</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-currency-rupee"></i></span>
                <input
                  class="form-control bg-light border-start-0 ps-0"
                  v-model="salary"
                  placeholder="e.g. 12 LPA"
                />
              </div>
            </div>

            <div class="col-12">
              <label class="form-label fw-semibold text-secondary small">Job Description</label>
              <textarea
                class="form-control bg-light"
                rows="3"
                v-model="job_description"
                placeholder="Key responsibilities, requirements, and role details..."
              ></textarea>
            </div>

            <div class="col-md-6">
              <label class="form-label fw-semibold text-secondary small">Eligibility Criteria</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-journal-check"></i></span>
                <input
                  class="form-control bg-light border-start-0 ps-0"
                  v-model="eligibility"
                  placeholder="e.g. CGPA >= 7.5, CSE/DS branch"
                />
              </div>
            </div>

            <div class="col-md-6">
              <label class="form-label fw-semibold text-secondary small">Application Deadline</label>
              <div class="input-group">
                <span class="input-group-text bg-light border-end-0 text-muted"><i class="bi bi-calendar-event"></i></span>
                <input
                  type="date"
                  class="form-control bg-light border-start-0 ps-0"
                  v-model="application_deadline"
                />
              </div>
            </div>
          </div>

          <button
            v-if="editingDriveId === null"
            class="btn btn-primary px-4 fw-medium rounded-2"
            @click="createDrive"
          >
            <i class="bi bi-plus-lg me-1"></i> Create Drive
          </button>

          <button
            v-else
            class="btn btn-success px-4 fw-medium rounded-2"
            @click="updateDrive"
          >
            <i class="bi bi-check-lg me-1"></i> Update Drive
          </button>
        </div>
      </div>

      <!-- Placement Drives Table Card -->
      <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-warning-subtle text-warning rounded-2 p-2">
            <i class="bi bi-briefcase"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">My Placement Drives</h5>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Job Title</th>
                <th>Eligibility</th>
                <th>Salary</th>
                <th>Deadline</th>
                <th>Status</th>
                <th>Approval</th>
                <th>Actions</th>
                <th>Applicants</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="drive in drives" :key="drive.id">
                <td class="ps-4 fw-semibold text-dark">{{ drive.job_title }}</td>
                <td><small class="text-muted">{{ drive.eligibility }}</small></td>
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
                  <div class="d-flex align-items-center gap-1">
                    <button
                      v-if="drive.status === 'Open'"
                      class="btn btn-outline-secondary btn-xs px-2 py-0-5"
                      @click="toggleStatus(drive.id)"
                    >
                      Close
                    </button>

                    <button
                      v-else
                      class="btn btn-outline-success btn-xs px-2 py-0-5"
                      @click="toggleStatus(drive.id)"
                    >
                      Open
                    </button>

                    <template v-if="drive.approval_status !== 'Approved'">
                      <button
                        class="btn btn-outline-warning btn-xs px-2 py-0-5"
                        @click="editDrive(drive)"
                      >
                        Edit
                      </button>

                      <button
                        class="btn btn-outline-danger btn-xs px-2 py-0-5"
                        @click="deleteDrive(drive.id)"
                      >
                        Delete
                      </button>
                    </template>

                    <span
                      v-else
                      class="badge bg-light text-muted border fs-8"
                    >
                      Locked
                    </span>
                  </div>
                </td>
                <td>
                  <button
                    v-if="drive.approval_status === 'Approved'"
                    class="btn btn-outline-primary btn-xs px-2 py-1"
                    @click="loadApplicants(drive)"
                  >
                    <i class="bi bi-people me-1"></i> View Applicants
                  </button>

                  <span
                    v-else
                    class="badge bg-light text-muted border fs-8"
                  >
                    Not Available
                  </span>
                </td>
              </tr>
              <tr v-if="drives.length === 0">
                <td colspan="8" class="text-center py-4 text-muted">No placement drives created yet</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Applicants List Section (when selectedDrive is active) -->
      <div
        v-if="selectedDrive"
        class="card border-0 shadow-sm rounded-3"
      >
        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
          <div class="icon-square bg-info-subtle text-info rounded-2 p-2">
            <i class="bi bi-person-check"></i>
          </div>
          <h5 class="fw-bold text-dark mb-0">
            Applicants for {{ selectedDrive.job_title }}
          </h5>
        </div>

        <div class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead class="bg-light">
              <tr>
                <th class="ps-4">Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Branch</th>
                <th>CGPA</th>
                <th>Skills</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="applicant in applicants"
                :key="applicant.application_id"
              >
                <td class="ps-4 fw-semibold text-dark">{{ applicant.student_name }}</td>
                <td><small class="text-muted">{{ applicant.email }}</small></td>
                <td><small class="text-muted">{{ applicant.phone }}</small></td>
                <td><span class="badge bg-light text-dark border">{{ applicant.branch }}</span></td>
                <td class="fw-bold text-primary">{{ applicant.cgpa }}</td>
                <td><small class="text-muted">{{ applicant.skills }}</small></td>
                <td>
                  <span
                    class="badge rounded-pill px-2-5 py-1"
                    :class="{
                      'bg-primary-subtle text-primary border border-primary-subtle': applicant.status === 'Applied',
                      'bg-warning-subtle text-warning border border-warning-subtle': applicant.status === 'Shortlisted',
                      'bg-success-subtle text-success border border-success-subtle': applicant.status === 'Selected',
                      'bg-danger-subtle text-danger border border-danger-subtle': applicant.status === 'Rejected'
                    }"
                  >
                    {{ applicant.status }}
                  </span>
                </td>
                <td>
                  <div class="d-flex align-items-center gap-1">
                    <button
                      v-if="applicant.resume"
                      class="btn btn-outline-info btn-xs px-2 py-0-5 me-1"
                      @click="viewStudentResume(applicant.student_id)"
                    >
                      <i class="bi bi-file-earmark-pdf me-1"></i> Resume
                    </button>

                    <template v-if="applicant.status === 'Applied'">
                      <button
                        class="btn btn-outline-success btn-xs px-2 py-0-5"
                        @click="shortlistApplicant(applicant.application_id)"
                      >
                        Shortlist
                      </button>

                      <button
                        class="btn btn-outline-danger btn-xs px-2 py-0-5"
                        @click="rejectApplicant(applicant.application_id)"
                      >
                        Reject
                      </button>
                    </template>

                    <template v-else-if="applicant.status === 'Shortlisted'">
                      <button
                        class="btn btn-outline-primary btn-xs px-2 py-0-5"
                        @click="openInterviewModal(applicant.application_id)"
                      >
                        <i class="bi bi-calendar-event me-1"></i> Interview
                      </button>

                      <button
                        class="btn btn-success btn-xs px-2 py-0-5"
                        @click="selectApplicant(applicant.application_id)"
                      >
                        Select
                      </button>

                      <button
                        class="btn btn-outline-danger btn-xs px-2 py-0-5"
                        @click="rejectApplicant(applicant.application_id)"
                      >
                        Reject
                      </button>
                    </template>

                    <span
                      v-else
                      class="badge bg-light text-muted border fs-8"
                    >
                      Final Decision
                    </span>
                  </div>
                </td>
              </tr>
              <tr v-if="applicants.length === 0">
                <td colspan="8" class="text-center py-4 text-muted">No applicants found for this drive</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- Interview Schedule Modal -->
    <div
      class="modal fade"
      id="interviewModal"
      tabindex="-1"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
          <div class="modal-header bg-dark text-white py-3">
            <h5 class="modal-title fw-bold fs-6">
              <i class="bi bi-calendar-event text-primary me-2"></i> Schedule Interview
            </h5>
            <button
              class="btn-close btn-close-white"
              data-bs-dismiss="modal"
            ></button>
          </div>

          <div class="modal-body p-4">
            <div class="mb-3">
              <label class="form-label fw-semibold text-secondary small">Interview Date</label>
              <input
                type="date"
                class="form-control bg-light"
                v-model="interviewForm.interview_date"
              >
            </div>

            <div class="mb-3">
              <label class="form-label fw-semibold text-secondary small">Interview Time</label>
              <input
                type="time"
                class="form-control bg-light"
                v-model="interviewForm.interview_time"
              >
            </div>

            <div class="mb-3">
              <label class="form-label fw-semibold text-secondary small">Interview Mode</label>
              <select
                class="form-select bg-light"
                v-model="interviewForm.interview_mode"
              >
                <option>Online</option>
                <option>Offline</option>
              </select>
            </div>

            <div class="mb-3">
              <label class="form-label fw-semibold text-secondary small">Location / Meeting Link</label>
              <input
                class="form-control bg-light"
                placeholder="Google Meet link or office address"
                v-model="interviewForm.interview_location"
              >
            </div>
          </div>

          <div class="modal-footer bg-light border-0 py-3">
            <button
              class="btn btn-secondary btn-sm px-3 rounded-2"
              data-bs-dismiss="modal"
            >
              Cancel
            </button>
            <button
              class="btn btn-success btn-sm px-4 rounded-2"
              @click="scheduleInterview"
            >
              <i class="bi bi-check-circle me-1"></i> Save Schedule
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import api from "../services/api";
import { ref, onMounted, reactive } from "vue";
import { useRouter } from "vue-router";
import * as bootstrap from "bootstrap";

const router = useRouter();
const job_title = ref("");
const job_description = ref("");
const eligibility = ref("");
const salary = ref("");
const application_deadline = ref("");
const drives = ref([]);
const editingDriveId = ref(null);
const applicants = ref([]);
const selectedDrive = ref(null);
const interviewForm = reactive({
  application_id: null,
  interview_date: "",
  interview_time: "",
  interview_mode: "Online",
  interview_location: ""
});
const companyProfile = reactive({
  company_name: "",
  industry: "",
  website: "",
  hr_name: "",
  hr_email: ""
});

const createDrive = async () => {
  try {
    await api.post("/company/drive", {
      job_title: job_title.value,
      job_description: job_description.value,
      eligibility: eligibility.value,
      salary: salary.value,
      application_deadline: application_deadline.value,
    });

    alert("Placement drive created successfully!");

    job_title.value = "";
    job_description.value = "";
    eligibility.value = "";
    salary.value = "";
    application_deadline.value = "";

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message || "Failed to create placement drive."
    );
  }
};

const updateDrive = async () => {
  try {
    await api.put(`/company/drive/${editingDriveId.value}`, {
      job_title: job_title.value,
      job_description: job_description.value,
      eligibility: eligibility.value,
      salary: salary.value,
      application_deadline: application_deadline.value,
    });

    alert("Placement drive updated successfully!");

    editingDriveId.value = null;

    job_title.value = "";
    job_description.value = "";
    eligibility.value = "";
    salary.value = "";
    application_deadline.value = "";

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message || "Failed to update placement drive."
    );
  }
};

const loadDrives = async () => {
  try {
    const response = await api.get("/company/drives");
    drives.value = response.data;

  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  loadCompanyProfile();
  loadDrives();
});

const deleteDrive = async (id) => {
  if (!confirm("Are you sure you want to delete this placement drive?")) {
    return;
  }

  try {
    await api.delete(`/company/drive/${id}`);

    alert("Placement drive deleted successfully!");

    await loadDrives();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to delete placement drive."
    );
  }
};

const toggleStatus = async (id) => {
  try {
    const response = await api.put(
      `/company/drive/${id}/toggle-status`
    );

    alert(response.data.message);

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to update drive status."
    );
  }
};

const editDrive = (drive) => {
  editingDriveId.value = drive.id;

  job_title.value = drive.job_title;
  job_description.value = drive.job_description;
  eligibility.value = drive.eligibility;
  salary.value = drive.salary;
  application_deadline.value = drive.application_deadline;
};

const loadApplicants = async (drive) => {
  try {
    const response = await api.get(
      `/company/drive/${drive.id}/applications`
    );

    applicants.value = response.data;
    selectedDrive.value = drive;

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load applicants."
    );
  }
};

const shortlistApplicant = async (applicationId) => {
  try {
    const response = await api.put(
      `/company/application/${applicationId}/shortlist`
    );

    alert(response.data.message);

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to shortlist applicant."
    );
  }
};

const selectApplicant = async (applicationId) => {
  try {
    const response = await api.put(
      `/company/application/${applicationId}/select`
    );

    alert(response.data.message);

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to select applicant."
    );
  }
};

function openInterviewModal(applicationId) {
  interviewForm.application_id = applicationId;
  interviewForm.interview_date = "";
  interviewForm.interview_time = "";
  interviewForm.interview_mode = "Online";
  interviewForm.interview_location = "";

  const modal = new bootstrap.Modal(
    document.getElementById("interviewModal")
  );

  modal.show();
}

const scheduleInterview = async () => {
  try {
    const response = await api.put(
      `/company/application/${interviewForm.application_id}/schedule-interview`,
      {
        interview_date: interviewForm.interview_date,
        interview_time: interviewForm.interview_time,
        interview_mode: interviewForm.interview_mode,
        interview_location: interviewForm.interview_location
      }
    );

    alert(response.data.message);

    bootstrap.Modal.getInstance(
      document.getElementById("interviewModal")
    ).hide();

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to schedule interview."
    );
  }
};

const rejectApplicant = async (applicationId) => {
  try {
    const response = await api.put(
      `/company/application/${applicationId}/reject`
    );

    alert(response.data.message);

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to reject applicant."
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

async function loadCompanyProfile() {
  try {
    const response = await api.get("/company/profile");

    Object.assign(companyProfile, response.data);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to load company profile."
    );
  }
}

async function updateCompanyProfile() {
  try {
    const response = await api.put(
      "/company/profile",
      companyProfile
    );

    alert(response.data.message);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to update company profile."
    );
  }
}

function viewStudentResume(studentId) {
  window.open(
    `http://localhost:5000/api/company/resume/${studentId}`,
    "_blank"
  );
}
</script>

<style scoped>
.company-dashboard-wrapper {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1e293b;
}

.bg-slate-50 {
  background-color: #f8fafc;
}

.bg-emerald {
  background-color: #10b981;
}

.bg-emerald-subtle {
  background-color: #dcfce7;
}

.text-emerald {
  color: #15803d;
}

.btn-emerald {
  background-color: #10b981;
  color: #ffffff;
  border: none;
}

.btn-emerald:hover {
  background-color: #059669;
  color: #ffffff;
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
</style>