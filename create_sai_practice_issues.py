#!/usr/bin/env python3
"""
Script to create GitHub issues for all Pure Mathematics papers for Sai Krishnamoorthy
"""

import os
import re
from datetime import datetime, timedelta

def parse_paper_info(filepath):
    """Extract paper information from filepath"""
    # Extract year, session, and paper from path like: 2024/Jun/11/9709_s24_qp_11.pdf
    parts = filepath.split('/')
    if len(parts) < 4:
        return None
    
    year = parts[0]
    session_folder = parts[1]
    paper_folder = parts[2]
    filename = parts[3]
    
    # Map session folders to session codes
    session_map = {
        'Mar': 'm',
        'Jun': 's', 
        'Oct': 'w'
    }
    
    session_code = session_map.get(session_folder, session_folder.lower())
    
    # Extract paper number from filename
    paper_match = re.search(r'9709_[msw]\d{2}_qp_(\d+)\.pdf', filename)
    if not paper_match:
        return None
    
    paper_num = paper_match.group(1)
    
    # Determine paper type
    paper_types = {
        '11': 'Paper 1: Pure Mathematics 1',
        '12': 'Paper 1: Pure Mathematics 1', 
        '13': 'Paper 1: Pure Mathematics 1'
    }
    
    paper_type = paper_types.get(paper_num, f'Paper {paper_num}')
    
    # Determine difficulty level based on paper and year
    if int(year) >= 2023:
        difficulty = 'Advanced'
    elif int(year) >= 2021:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Beginner'
    
    return {
        'year': year,
        'session': session_folder,
        'session_code': session_code,
        'paper_num': paper_num,
        'paper_type': paper_type,
        'difficulty': difficulty,
        'paper_id': f"{session_code}{year[-2:]}/{paper_num}"
    }

def generate_issue_content(paper_info):
    """Generate GitHub issue content for a paper"""
    
    # Calculate target completion date (7 days from now)
    target_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    
    # Determine time allocation based on paper type
    time_allocation = "1h 50min"  # Standard for Pure Math papers
    
    title = f"[Sai Krishnamoorthy] [Pure-Math-9709] [{paper_info['paper_id']}] - Practice Session"
    
    content = f"""## Student Practice Session

**Student**: Sai Krishnamoorthy
**Paper**: 9709/{paper_info['paper_id']} (Pure Mathematics {paper_info['paper_num']})
**Paper Type**: {paper_info['paper_type']}
**Assigned Date**: {datetime.now().strftime('%Y-%m-%d')}
**Target Completion**: {target_date}
**Difficulty Level**: {paper_info['difficulty']}

---

## Practice Session Details

- **Time Allocated**: {time_allocation}
- **Practice Mode**: Timed Exam
- **Resources Allowed**: Formula Sheet Only

---

## Pre-Practice Checklist

- [ ] Student has reviewed relevant theory
- [ ] Previous similar papers completed
- [ ] Weak areas identified from last session
- [ ] Timer/environment set up
- [ ] Question paper and answer sheet ready

---

## Practice Session Results

### Performance Tracking
- **Score Achieved**: ___/75
- **Percentage**: ___%
- **Time Taken**: <!-- Actual time taken -->
- **Grade Equivalent**: <!-- A*/A/B/C/D/E -->

### Topic Performance Breakdown
- [ ] **Algebra**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Functions**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Coordinate Geometry**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Sequences & Series**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Trigonometry**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Differentiation**: ___/<!-- marks --> - <!-- Comments -->
- [ ] **Integration**: ___/<!-- marks --> - <!-- Comments -->

---

## Analysis & Feedback

### Areas of Strength
<!-- List areas where student performed well -->
- 
- 
- 

### Areas for Improvement
<!-- List areas needing work -->
- 
- 
- 

### Teacher/Tutor Comments
<!-- Detailed feedback on performance -->


### Student Self-Assessment
<!-- Student's own reflection on the practice session -->


---

## Post-Practice Checklist

- [ ] Paper completed and submitted
- [ ] Self-assessment completed
- [ ] Teacher review completed
- [ ] Feedback discussion held
- [ ] Next steps identified
- [ ] Performance data recorded

---

## Action Plan

### Immediate Actions (This Week)
- [ ] Review specific topics: <!-- List topics -->
- [ ] Practice similar questions from: <!-- Specify sources -->
- [ ] Complete additional exercises on: <!-- Weak areas -->

### Follow-up Actions (Next Week)
- [ ] Schedule follow-up practice session
- [ ] Retry similar difficulty paper
- [ ] Move to next topic/paper level

### Additional Resources Needed
- [ ] <!-- List any additional study materials, tutoring, etc. -->

---

## Progress Notes
<!-- Track progress over multiple sessions -->

**Previous Session Score**: <!-- If applicable -->
**Improvement**: <!-- +/- percentage points -->
**Trend**: <!-- Improving | Stable | Declining -->

---

## Labels to Add
<!-- These will be added automatically -->

**Student Level:**
- [x] `{paper_info['difficulty'].lower()}`

**Performance:**
- [ ] `excellent` (90%+)
- [ ] `good` (75-89%)
- [ ] `needs-improvement` (60-74%)
- [ ] `requires-support` (<60%)

**Priority:**
- [ ] `urgent-practice`
- [ ] `focus-area`
- [ ] `progress-check`

**Subject:**
- [x] `pure-mathematics-9709`
- [x] `practice-session`
- [x] `student-sai-krishnamoorthy`
"""
    
    return title, content

def main():
    """Main function to process all papers and generate issue content"""
    
    # List of all available papers based on the file listing
    papers = [
        # 2019
        "2019/Jun/11/9709_s19_qp_11.pdf",
        "2019/Jun/12/9709_s19_qp_12.pdf", 
        "2019/Jun/13/9709_s19_qp_13.pdf",
        "2019/Mar/12/9709_m19_qp_12.pdf",
        "2019/Oct/11/9709_w19_qp_11.pdf",
        "2019/Oct/12/9709_w19_qp_12.pdf",
        "2019/Oct/13/9709_w19_qp_13.pdf",
        
        # 2020
        "2020/Jun/11/9709_s20_qp_11.pdf",
        "2020/Jun/12/9709_s20_qp_12.pdf",
        "2020/Jun/13/9709_s20_qp_13.pdf", 
        "2020/Mar/12/9709_m20_qp_12.pdf",
        
        # 2021
        "2021/Jun/11/9709_s21_qp_11.pdf",
        "2021/Jun/12/9709_s21_qp_12.pdf",
        "2021/Jun/13/9709_s21_qp_13.pdf",
        "2021/Mar/12/9709_m21_qp_12.pdf",
        
        # 2022
        "2022/Jun/11/9709_s22_qp_11.pdf",
        "2022/Jun/12/9709_s22_qp_12.pdf", 
        "2022/Jun/13/9709_s22_qp_13.pdf",
        "2022/Mar/12/9709_m22_qp_12.pdf",
        
        # 2023
        "2023/Jun/11/9709_s23_qp_11.pdf",
        "2023/Jun/12/9709_s23_qp_12.pdf",
        "2023/Jun/13/9709_s23_qp_13.pdf",
        "2023/Mar/12/9709_m23_qp_12.pdf",
        "2023/Oct/13/9709_w23_qp_13.pdf",
        
        # 2024
        "2024/Jun/11/9709_s24_qp_11.pdf",
        "2024/Jun/12/9709_s24_qp_12.pdf",
        "2024/Jun/13/9709_s24_qp_13.pdf",
        "2024/Mar/12/9709_m24_qp_12.pdf",
        "2024/Oct/11/9709_w24_qp_11.pdf",
        "2024/Oct/12/9709_w24_qp_12.pdf",
        "2024/Oct/13/9709_w24_qp_13.pdf",
        
        # 2025
        "2025/Jun/11/9709_s25_qp_11.pdf",
        "2025/Jun/12/9709_s25_qp_12.pdf", 
        "2025/Jun/13/9709_s25_qp_13.pdf",
        "2025/Mar/12/9709_m25_qp_12.pdf"
    ]
    
    print(f"Found {len(papers)} Pure Mathematics papers for Sai Krishnamoorthy")
    print("=" * 60)
    
    issues_created = 0
    
    for paper_path in papers:
        paper_info = parse_paper_info(paper_path)
        if paper_info:
            title, content = generate_issue_content(paper_info)
            
            # Create markdown file for each issue
            filename = f"issue_{paper_info['year']}_{paper_info['session']}_{paper_info['paper_num']}.md"
            
            with open(f"sai_practice_issues/{filename}", 'w') as f:
                f.write(f"# {title}\n\n")
                f.write(content)
            
            print(f"✓ Created: {title}")
            issues_created += 1
    
    print("=" * 60)
    print(f"Successfully created {issues_created} practice session issues for Sai Krishnamoorthy")
    print(f"Files saved in: sai_practice_issues/")
    print("\nNext steps:")
    print("1. Review the generated issue files")
    print("2. Create GitHub issues manually using the content from each file")
    print("3. Apply appropriate labels: pure-mathematics-9709, practice-session, student-sai-krishnamoorthy")

if __name__ == "__main__":
    # Create output directory
    os.makedirs("sai_practice_issues", exist_ok=True)
    main()
