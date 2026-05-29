#====================================================================================================
# START - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================

# THIS SECTION CONTAINS CRITICAL TESTING INSTRUCTIONS FOR BOTH AGENTS
# BOTH MAIN_AGENT AND TESTING_AGENT MUST PRESERVE THIS ENTIRE BLOCK

# Communication Protocol:
# If the `testing_agent` is available, main agent should delegate all testing tasks to it.
#
# You have access to a file called `test_result.md`. This file contains the complete testing state
# and history, and is the primary means of communication between main and the testing agent.
#
# Main and testing agents must follow this exact format to maintain testing data. 
# The testing data must be entered in yaml format Below is the data structure:
# 
## user_problem_statement: {problem_statement}
## backend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.py"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## frontend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.js"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## metadata:
##   created_by: "main_agent"
##   version: "1.0"
##   test_sequence: 0
##   run_ui: false
##
## test_plan:
##   current_focus:
##     - "Task name 1"
##     - "Task name 2"
##   stuck_tasks:
##     - "Task name with persistent issues"
##   test_all: false
##   test_priority: "high_first"  # or "sequential" or "stuck_first"
##
## agent_communication:
##     -agent: "main"  # or "testing" or "user"
##     -message: "Communication message between agents"

# Protocol Guidelines for Main agent
#
# 1. Update Test Result File Before Testing:
#    - Main agent must always update the `test_result.md` file before calling the testing agent
#    - Add implementation details to the status_history
#    - Set `needs_retesting` to true for tasks that need testing
#    - Update the `test_plan` section to guide testing priorities
#    - Add a message to `agent_communication` explaining what you've done
#
# 2. Incorporate User Feedback:
#    - When a user provides feedback that something is or isn't working, add this information to the relevant task's status_history
#    - Update the working status based on user feedback
#    - If a user reports an issue with a task that was marked as working, increment the stuck_count
#    - Whenever user reports issue in the app, if we have testing agent and task_result.md file so find the appropriate task for that and append in status_history of that task to contain the user concern and problem as well 
#
# 3. Track Stuck Tasks:
#    - Monitor which tasks have high stuck_count values or where you are fixing same issue again and again, analyze that when you read task_result.md
#    - For persistent issues, use websearch tool to find solutions
#    - Pay special attention to tasks in the stuck_tasks list
#    - When you fix an issue with a stuck task, don't reset the stuck_count until the testing agent confirms it's working
#
# 4. Provide Context to Testing Agent:
#    - When calling the testing agent, provide clear instructions about:
#      - Which tasks need testing (reference the test_plan)
#      - Any authentication details or configuration needed
#      - Specific test scenarios to focus on
#      - Any known issues or edge cases to verify
#
# 5. Call the testing agent with specific instructions referring to test_result.md
#
# IMPORTANT: Main agent must ALWAYS update test_result.md BEFORE calling the testing agent, as it relies on this file to understand what to test next.

#====================================================================================================
# END - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================



#====================================================================================================
# Testing Data - Main Agent and testing sub agent both should log testing data below this section
#====================================================================================================

user_problem_statement: |
  Produce two branded documents comparing the TMHCC Media & Music Combined wording against
  competitor wordings (Tysers/Zurich, Yutree/AXA, Liberty, Allianz; fifth competitor pending):
  (1) Full Coverage Comparison and (2) Gap-Fill / Wording Enhancement Strategy, plus a QA report.
  The three new branded documents (docx + pdf) must be added to the in-app Document Centre so the
  user can download them from the Preview.

backend:
  - task: "Document Centre API exposes the 3 new comparison documents with groups + downloads"
    implemented: true
    working: true
    file: "/app/backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        -working: "NA"
        -agent: "main"
        -comment: |
          Round 7: added 3 comparison documents to DOCUMENTS, served 7 docs total. Original detail:
          with a 'group' field ("Media & Entertainment — market comparison"); existing 4 wording docs
          default to group "Media & Music Combined wording (0526)". GET /api/documents should now return
          7 documents, each with a non-empty 'group' and a 'formats' array containing BOTH docx and pdf
          (with size_kb). GET /api/documents/download/{filename} should return the new files with the
          correct media type for these base names:
            TMHCC_Media_Coverage_Comparison_FULL(.docx/.pdf)
            TMHCC_Media_GapFill_Enhancement_Strategy(.docx/.pdf)
            TMHCC_Media_Comparison_QA_Methodology(.docx/.pdf)
          Files exist in /app/backend/deliverables. Please verify status 200, correct content-type
          (docx => wordprocessingml.document, pdf => application/pdf) and that a 404 is returned for a
          bad filename / unsupported extension.
        -working: true
        -agent: "testing"
        -comment: |
          ✅ ALL BACKEND TESTS PASSED (32/32 tests) — see prior run.
        -working: "NA"
        -agent: "main"
        -comment: |
          ROUND 8 (EMERGENT DISPATCH v3): regenerated all deliverables and REFRESHED the DOCUMENTS metadata.
          GET /api/documents should now return 9 documents. Titles/descriptions updated:
            comparison_full   -> "Full Coverage Comparison (Client / Broker)"
            comparison_gapfill-> "Full Gap Analysis (Internal)"
            comparison_qa     -> "QA / Change Report"
            wording_tracked   -> "Final Wording (0526) — Tracked Changes (Round 8)"
            wording_clean     -> "Final Wording (0526) — Clean (Round 8)"
          The underlying files in /app/backend/deliverables were overwritten with the Round-8 versions
          (same base filenames). Please verify GET /api/documents returns 9 docs, each with a 'formats'
          array containing BOTH docx and pdf (size_kb > 0), and that GET /api/documents/download/{filename}
          returns 200 with the correct content-type for these Round-8 base names (docx + pdf):
            TMHCC_Media_Combined_0526_FINAL_TrackedChanges, TMHCC_Media_Combined_0526_FINAL_Clean,
            TMHCC_Media_Coverage_Comparison_FULL, TMHCC_Media_GapFill_Enhancement_Strategy,
            TMHCC_Media_Comparison_QA_Methodology, TMHCC_Media_Combined_Summary_of_Changes_FINAL,
            TMHCC_Media_Combined_Summary_of_Cover_FINAL. Confirm 404 for a bad filename. Backend only.
        -working: true
        -agent: "testing"
        -comment: |
          ✅ ALL BACKEND TESTS PASSED (88/88 tests) — Round 8 verification complete.
          
          COMPREHENSIVE TEST RESULTS:
          
          1. GET /api/documents endpoint (51 tests passed):
             ✅ Returns HTTP 200 with correct JSON structure
             ✅ Returns EXACTLY 9 documents as expected
             ✅ All 9 expected document IDs present: comparison_full, comparison_gapfill, comparison_qa,
                wording_tracked, wording_clean, wording, changes, cover, qa
             ✅ All documents have required fields: id, title, subtitle, description, accent, formats
             ✅ Round 8 title updates verified:
                - comparison_full contains "Client / Broker" ✓
                - comparison_gapfill contains "Gap Analysis (Internal)" ✓
                - wording_tracked contains "Round 8" ✓
                - wording_clean contains "Round 8" ✓
             ✅ All documents have non-empty formats array with BOTH docx and pdf
             ✅ All format entries have size_kb > 0 (verified for all 18 files)
          
          2. GET /api/documents/download/{filename} endpoint (35 tests passed):
             ✅ All 14 files (7 base names × 2 formats) download successfully with HTTP 200
             ✅ Correct Content-Type headers for all files:
                - .docx files: application/vnd.openxmlformats-officedocument.wordprocessingml.document
                - .pdf files: application/pdf
             ✅ All files have non-empty bodies (verified byte counts)
             ✅ Files tested:
                - TMHCC_Media_Combined_0526_FINAL_TrackedChanges (.docx, .pdf)
                - TMHCC_Media_Combined_0526_FINAL_Clean (.docx, .pdf)
                - TMHCC_Media_Coverage_Comparison_FULL (.docx, .pdf)
                - TMHCC_Media_GapFill_Enhancement_Strategy (.docx, .pdf)
                - TMHCC_Media_Comparison_QA_Methodology (.docx, .pdf)
                - TMHCC_Media_Combined_Summary_of_Changes_FINAL (.docx, .pdf)
                - TMHCC_Media_Combined_Summary_of_Cover_FINAL (.docx, .pdf)
          
          3. Error handling (2 tests passed):
             ✅ Returns HTTP 404 for non-existent file (does_not_exist.docx)
             ✅ Returns HTTP 404 for unsupported extension/path traversal (server.py)
          
          The Document Centre API backend is fully functional and production-ready for Round 8.

frontend:
  - task: "Document Centre groups documents into two sections and lists the 3 new docs"
    implemented: true
    working: "NA"
    file: "/app/frontend/src/App.js"
    stuck_count: 0
    priority: "medium"
    needs_retesting: false
    status_history:
        -working: "NA"
        -agent: "main"
        -comment: |
          Frontend now groups docs by 'group' with section headings. NOT to be tested until the user
          approves frontend testing.

metadata:
  created_by: "main_agent"
  version: "1.0"
  test_sequence: 3
  run_ui: false

test_plan:
  current_focus: []
  stuck_tasks: []
  test_all: false
  test_priority: "high_first"

agent_communication:
    -agent: "main"
    -message: |
      Please test the BACKEND ONLY. Verify GET /api/documents returns 7 documents, each with a
      'group' and 'formats' (docx + pdf, size_kb > 0). Then verify GET /api/documents/download/{filename}
      returns 200 with the correct content-type for the 3 NEW base names (both docx and pdf), and 404
      for a non-existent filename. Do not test the frontend.
    -agent: "testing"
    -message: |
      ✅ BACKEND TESTING COMPLETE - ALL TESTS PASSED
      
      Comprehensive testing completed on Document Centre API endpoints. All 32 tests passed successfully:
      
      1. GET /api/documents endpoint fully functional:
         - Returns 7 documents with correct structure
         - All 3 new comparison documents present with correct groups
         - All 4 existing wording documents have correct groups
         - All documents have both docx and pdf formats with valid sizes
      
      2. GET /api/documents/download/{filename} endpoint fully functional:
         - All 6 new document files (3 docs × 2 formats) download successfully
         - Correct Content-Type headers for all files
         - All files have non-empty bodies
      
      3. Error handling working correctly:
         - Returns 404 for non-existent files
         - Returns 404 for unsupported extensions/path traversal attempts
      
      The backend implementation is production-ready and meets all specified requirements.
    -agent: "main"
    -message: |
      ROUND 8 (v3): Document Centre metadata refreshed and all deliverable files overwritten with Round-8
      versions (same base filenames). Please test BACKEND ONLY: GET /api/documents now returns 9 documents,
      each with a 'formats' array containing BOTH docx and pdf (size_kb > 0). Verify
      GET /api/documents/download/{filename} returns 200 + correct content-type (docx => wordprocessingml.document,
      pdf => application/pdf) for the Round-8 base names: TMHCC_Media_Combined_0526_FINAL_TrackedChanges,
      TMHCC_Media_Combined_0526_FINAL_Clean, TMHCC_Media_Coverage_Comparison_FULL,
      TMHCC_Media_GapFill_Enhancement_Strategy, TMHCC_Media_Comparison_QA_Methodology,
      TMHCC_Media_Combined_Summary_of_Changes_FINAL, TMHCC_Media_Combined_Summary_of_Cover_FINAL
      (both docx and pdf each), and 404 for a non-existent filename. Do not test the frontend.
    -agent: "testing"
    -message: |
      ✅ ROUND 8 BACKEND TESTING COMPLETE - ALL 88 TESTS PASSED
      
      Comprehensive backend testing completed for Document Centre API Round 8 update. Zero failures.
      
      DETAILED RESULTS:
      
      1. GET /api/documents (51 tests):
         ✅ Returns exactly 9 documents (up from 7 in Round 7)
         ✅ All 9 expected document IDs present and verified
         ✅ Round 8 title updates confirmed:
            • comparison_full: "Client / Broker" ✓
            • comparison_gapfill: "Gap Analysis (Internal)" ✓
            • wording_tracked: "Round 8" ✓
            • wording_clean: "Round 8" ✓
         ✅ All documents have complete structure (id, title, subtitle, description, accent, formats)
         ✅ All 9 documents have both docx and pdf formats with size_kb > 0
      
      2. GET /api/documents/download/{filename} (35 tests):
         ✅ All 14 files (7 base names × 2 formats) download successfully
         ✅ Correct Content-Type headers verified for all files
         ✅ All files have non-empty bodies with correct byte counts
         ✅ Tested files: TrackedChanges, Clean, Comparison_FULL, GapFill, QA, Changes, Cover
      
      3. Error handling (2 tests):
         ✅ HTTP 404 for non-existent files
         ✅ HTTP 404 for unsupported extensions/path traversal
      
      The Document Centre API backend is fully functional and production-ready for Round 8.
