# Binary Files and Duplicates Audit Report

## Large Binary Files Found

### ZIP Files
1. **cyber_threats_and_vulnerabilities_2.zip** (1.3K) - Small, likely essential
2. **6d0875ec12b1e0fb5b2b3cc6c9e056d0fda67ec570ec4be0294568b80c87f576.zip** (814K) - Malware sample, essential for cybersecurity project
3. **security_operation_center1.zip** (2.1M) - Large project archive, review needed
4. **cybersecurity_project_v3.zip** (240K) - Project archive, review needed

### Audio Files
1. **SOC_podcast_spanish.wav** (22M) - Very large audio file, consider removal

## Duplicate Files Analysis

### Photo Duplicates in career_focus/edits/
Multiple versions of the same photos with "copy" suffixes:
- DSC06242 copy.jpg, DSC06243 copy.jpg, DSC06249 copy.jpg, etc.
- IMG_5047 copy.jpg, IMG_5400.JPG copy.jpg, etc.
- Multiple versions: IMG_7667 copy 2.jpg, IMG_7667 copy 3.jpg, IMG_7667 copy n2.jpg

### Document Duplicates
1. **README copy.md** in security_operation_center_1/
2. **Project Design Documentation copy.docx** in career_focus/Documentation/
3. **How to build a virtual lab step-by-step copy.pdf** in career_focus/virtual-lab-tools/

### Python File Versions
Multiple versions of doggy.py in both python_1/ and python_2/:
- doggy_v2.py through doggy_v7.0.py (duplicated in both folders)

## Recommendations

### Files to Remove (High Priority)
1. **SOC_podcast_spanish.wav** (22M) - Too large for repository
2. **All photo copies** in career_focus/edits/ - Keep only originals
3. **Document copies** - Merge with originals or remove
4. **Old Python versions** - Keep only latest (v7.0) in each folder

### Files to Keep (Essential)
1. **Malware sample zip** - Essential for cybersecurity analysis project
2. **Small project zips** - May contain important project deliverables

### Files Requiring Manual Review
1. **security_operation_center1.zip** (2.1M) - Check if contents are already in repository
2. **cybersecurity_project_v3.zip** (240K) - Check if contents are already in repository
##
 Actions Taken

### Files Removed
1. ✅ **SOC_podcast_spanish.wav** (22M) - Removed large audio file
2. ✅ **README copy.md** - Removed duplicate README
3. ✅ **Project Design Documentation copy.docx** - Removed duplicate document
4. ✅ **How to build a virtual lab step-by-step copy.pdf** - Removed duplicate PDF
5. ✅ **All photo copies** in career_focus/edits/ - Removed ~20 duplicate photos
6. ✅ **Old Python versions** - Removed doggy_v2.py through doggy_v6.py, kept only v7.0
7. ✅ **doggt_v3.py** - Removed typo version in both python folders

### Files Kept (Essential Binary Files)
1. **6d0875ec12b1e0fb5b2b3cc6c9e056d0fda67ec570ec4be0294568b80c87f576.zip** (814K) - Malware sample for cybersecurity analysis
2. **cyber_threats_and_vulnerabilities_2.zip** (1.3K) - Small project file
3. **cybersecurity_project_v3.zip** (240K) - Project deliverable
4. **security_operation_center1.zip** (2.1M) - Project deliverable

### Summary
- Removed approximately 22MB+ of unnecessary files
- Eliminated ~25 duplicate files
- Kept essential binary files for project functionality
- Maintained clean Python project structure with latest versions only