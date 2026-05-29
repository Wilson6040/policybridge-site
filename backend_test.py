#!/usr/bin/env python3
"""
Backend API Testing for Document Centre - Round 8
Tests the FastAPI backend endpoints for document listing and downloads.
"""

import requests
import sys
import os
from typing import Dict, List, Any

# Get backend URL from environment
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://policy-workflow-1.preview.emergentagent.com')
BASE_URL = f"{BACKEND_URL}/api"

# Expected 9 document IDs for Round 8
EXPECTED_DOC_IDS = [
    "comparison_full",
    "comparison_gapfill", 
    "comparison_qa",
    "wording_tracked",
    "wording_clean",
    "wording",
    "changes",
    "cover",
    "qa"
]

# Expected title updates for Round 8
TITLE_CHECKS = {
    "comparison_full": "Client / Broker",
    "comparison_gapfill": "Gap Analysis (Internal)",
    "wording_tracked": "Round 8",
    "wording_clean": "Round 8"
}

# Expected download files for Round 8 (7 base names × 2 formats = 14 files)
DOWNLOAD_FILES = [
    ("TMHCC_Media_Combined_0526_FINAL_TrackedChanges.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Combined_0526_FINAL_TrackedChanges.pdf", "application/pdf"),
    ("TMHCC_Media_Combined_0526_FINAL_Clean.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Combined_0526_FINAL_Clean.pdf", "application/pdf"),
    ("TMHCC_Media_Coverage_Comparison_FULL.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Coverage_Comparison_FULL.pdf", "application/pdf"),
    ("TMHCC_Media_GapFill_Enhancement_Strategy.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_GapFill_Enhancement_Strategy.pdf", "application/pdf"),
    ("TMHCC_Media_Comparison_QA_Methodology.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Comparison_QA_Methodology.pdf", "application/pdf"),
    ("TMHCC_Media_Combined_Summary_of_Changes_FINAL.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Combined_Summary_of_Changes_FINAL.pdf", "application/pdf"),
    ("TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ("TMHCC_Media_Combined_Summary_of_Cover_FINAL.pdf", "application/pdf"),
]

class TestResults:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def add_pass(self, test_name: str, details: str = ""):
        self.passed.append((test_name, details))
        print(f"✅ PASS: {test_name}")
        if details:
            print(f"   {details}")
    
    def add_fail(self, test_name: str, details: str):
        self.failed.append((test_name, details))
        print(f"❌ FAIL: {test_name}")
        print(f"   {details}")
    
    def add_warning(self, test_name: str, details: str):
        self.warnings.append((test_name, details))
        print(f"⚠️  WARNING: {test_name}")
        print(f"   {details}")
    
    def summary(self):
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)
        print(f"Total Passed: {len(self.passed)}")
        print(f"Total Failed: {len(self.failed)}")
        print(f"Total Warnings: {len(self.warnings)}")
        
        if self.failed:
            print("\n❌ FAILED TESTS:")
            for test_name, details in self.failed:
                print(f"  - {test_name}")
                print(f"    {details}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for test_name, details in self.warnings:
                print(f"  - {test_name}")
                print(f"    {details}")
        
        return len(self.failed) == 0


def test_documents_list(results: TestResults):
    """Test GET /api/documents endpoint"""
    print("\n" + "="*80)
    print("TEST 1: GET /api/documents")
    print("="*80)
    
    try:
        response = requests.get(f"{BASE_URL}/documents", timeout=10)
        
        # Check status code
        if response.status_code != 200:
            results.add_fail(
                "GET /api/documents - Status Code",
                f"Expected 200, got {response.status_code}"
            )
            return
        
        results.add_pass("GET /api/documents - Status Code", "200 OK")
        
        # Parse JSON
        try:
            data = response.json()
        except Exception as e:
            results.add_fail("GET /api/documents - JSON Parse", f"Failed to parse JSON: {e}")
            return
        
        # Check structure
        if "documents" not in data:
            results.add_fail(
                "GET /api/documents - Response Structure",
                "Missing 'documents' key in response"
            )
            return
        
        results.add_pass("GET /api/documents - Response Structure", "Has 'documents' key")
        
        documents = data["documents"]
        
        # Check document count - MUST be exactly 9 for Round 8
        if len(documents) != 9:
            results.add_fail(
                "GET /api/documents - Document Count",
                f"Expected EXACTLY 9 documents, got {len(documents)}"
            )
        else:
            results.add_pass("GET /api/documents - Document Count", "EXACTLY 9 documents returned")
        
        # Check each document structure
        found_ids = set()
        
        for doc in documents:
            doc_id = doc.get("id")
            found_ids.add(doc_id)
            
            # Check required fields
            required_fields = ["id", "title", "subtitle", "description", "accent", "formats"]
            missing_fields = [f for f in required_fields if not doc.get(f)]
            
            if missing_fields:
                results.add_fail(
                    f"Document '{doc_id}' - Required Fields",
                    f"Missing fields: {', '.join(missing_fields)}"
                )
                continue
            
            results.add_pass(
                f"Document '{doc_id}' - Required Fields",
                "All required fields present"
            )
            
            # Check title updates for Round 8
            if doc_id in TITLE_CHECKS:
                expected_substring = TITLE_CHECKS[doc_id]
                actual_title = doc.get("title", "")
                if expected_substring not in actual_title:
                    results.add_fail(
                        f"Document '{doc_id}' - Title Update",
                        f"Expected title to contain '{expected_substring}', got '{actual_title}'"
                    )
                else:
                    results.add_pass(
                        f"Document '{doc_id}' - Title Update",
                        f"Title correctly contains '{expected_substring}'"
                    )
            
            # Check formats array
            formats = doc.get("formats", [])
            if not isinstance(formats, list):
                results.add_fail(
                    f"Document '{doc_id}' - Formats",
                    "Formats is not an array"
                )
                continue
            
            if len(formats) == 0:
                results.add_fail(
                    f"Document '{doc_id}' - Formats",
                    "Formats array is empty"
                )
                continue
            
            # Check for both docx and pdf
            format_exts = {f.get("ext") for f in formats}
            if "docx" not in format_exts or "pdf" not in format_exts:
                results.add_fail(
                    f"Document '{doc_id}' - Formats",
                    f"Missing docx or pdf. Found: {format_exts}"
                )
            else:
                results.add_pass(
                    f"Document '{doc_id}' - Formats",
                    "Has BOTH docx and pdf"
                )
            
            # Check size_kb > 0 for all formats
            for fmt in formats:
                ext = fmt.get("ext")
                size_kb = fmt.get("size_kb", 0)
                if size_kb <= 0:
                    results.add_fail(
                        f"Document '{doc_id}' - Format {ext} size",
                        f"size_kb is {size_kb}, expected > 0"
                    )
                else:
                    results.add_pass(
                        f"Document '{doc_id}' - Format {ext} size",
                        f"size_kb = {size_kb} (> 0)"
                    )
        
        # Check all expected document IDs are present
        missing_ids = set(EXPECTED_DOC_IDS) - found_ids
        if missing_ids:
            results.add_fail(
                "GET /api/documents - Missing Documents",
                f"Missing document IDs: {', '.join(missing_ids)}"
            )
        else:
            results.add_pass(
                "GET /api/documents - All Expected IDs Present",
                f"All 9 expected document IDs found: {', '.join(EXPECTED_DOC_IDS)}"
            )
        
        # Check for unexpected document IDs
        unexpected_ids = found_ids - set(EXPECTED_DOC_IDS)
        if unexpected_ids:
            results.add_warning(
                "GET /api/documents - Unexpected Documents",
                f"Found unexpected document IDs: {', '.join(unexpected_ids)}"
            )
        
    except requests.exceptions.RequestException as e:
        results.add_fail("GET /api/documents - Request", f"Request failed: {e}")
    except Exception as e:
        results.add_fail("GET /api/documents - Unexpected Error", f"Error: {e}")


def test_document_downloads(results: TestResults):
    """Test GET /api/documents/download/{filename} endpoint"""
    print("\n" + "="*80)
    print("TEST 2: GET /api/documents/download/{filename}")
    print("="*80)
    
    # Test each of the 14 document files (7 base names × 2 formats)
    for filename, expected_content_type in DOWNLOAD_FILES:
        try:
            response = requests.get(
                f"{BASE_URL}/documents/download/{filename}",
                timeout=10
            )
            
            # Check status code
            if response.status_code != 200:
                results.add_fail(
                    f"Download '{filename}' - Status Code",
                    f"Expected 200, got {response.status_code}"
                )
                continue
            
            results.add_pass(
                f"Download '{filename}' - Status Code",
                "200 OK"
            )
            
            # Check content type
            actual_content_type = response.headers.get("content-type", "")
            if expected_content_type not in actual_content_type:
                results.add_fail(
                    f"Download '{filename}' - Content-Type",
                    f"Expected '{expected_content_type}', got '{actual_content_type}'"
                )
            else:
                results.add_pass(
                    f"Download '{filename}' - Content-Type",
                    f"Correct: {expected_content_type}"
                )
            
            # Check body is non-empty
            if len(response.content) == 0:
                results.add_fail(
                    f"Download '{filename}' - Body",
                    "Response body is empty"
                )
            else:
                results.add_pass(
                    f"Download '{filename}' - Body",
                    f"Non-empty ({len(response.content)} bytes)"
                )
        
        except requests.exceptions.RequestException as e:
            results.add_fail(f"Download '{filename}' - Request", f"Request failed: {e}")
        except Exception as e:
            results.add_fail(f"Download '{filename}' - Unexpected Error", f"Error: {e}")


def test_download_errors(results: TestResults):
    """Test error cases for document downloads"""
    print("\n" + "="*80)
    print("TEST 3: Download Error Cases")
    print("="*80)
    
    # Test 404 for non-existent file
    try:
        response = requests.get(
            f"{BASE_URL}/documents/download/does_not_exist.docx",
            timeout=10
        )
        
        if response.status_code == 404:
            results.add_pass(
                "Download non-existent file - Status Code",
                "Correctly returns 404"
            )
        else:
            results.add_fail(
                "Download non-existent file - Status Code",
                f"Expected 404, got {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        results.add_fail("Download non-existent file - Request", f"Request failed: {e}")
    
    # Test 404 for unsupported extension / path traversal
    try:
        response = requests.get(
            f"{BASE_URL}/documents/download/server.py",
            timeout=10
        )
        
        if response.status_code == 404:
            results.add_pass(
                "Download unsupported extension - Status Code",
                "Correctly returns 404 for server.py"
            )
        else:
            results.add_fail(
                "Download unsupported extension - Status Code",
                f"Expected 404, got {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        results.add_fail("Download unsupported extension - Request", f"Request failed: {e}")


def main():
    print("="*80)
    print("BACKEND API TESTING - DOCUMENT CENTRE (ROUND 8)")
    print("="*80)
    print(f"Backend URL: {BASE_URL}")
    print()
    
    results = TestResults()
    
    # Run all tests
    test_documents_list(results)
    test_document_downloads(results)
    test_download_errors(results)
    
    # Print summary
    success = results.summary()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
