#!/usr/bin/env python3
"""
Script to create GitHub issues for all Probability & Statistics papers for Sai Krishnamoorthy
"""

import os
import re
from datetime import datetime, timedelta

def parse_paper_info(filepath):
    """Extract paper information from filepath"""
    # Extract year, session, and paper from path like: 2024/Jun/51/9709_s24_qp_51.pdf
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
    
    # Determine paper type for Statistics papers (51, 52, 53)
    paper_types = {
        '51': 'Paper 5: Probability & Statistics 1',
        '52': 'Paper 5: Probability & Statistics 1', 
        '53': 'Paper 5: Probability & Statistics 1'
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
    """Generate GitHub issue content for a statistics paper"""
    
    # Calculate target completion date (7 days from now)
    target_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    
    # Determine time allocation based on paper type (Statistics papers are typically shorter)
    time_allocation = "1h 15min"  # Standard for Statistics papers
    
    title = f"[Sai Krishnamoorthy] [Probability-Statistics-9709] [{paper_info['paper_id']}] - Practice Session"
    
    content = f"""## Student Practice Session

**Student**: Sai Krishnamoorthy
**Paper**: 9709/{paper_info['paper_id']} (Probability & Statistics {paper_info['paper_num']})
**Paper Type**: {paper_info['paper_type']}
**Assigned Date**: {datetime.now().strftime('%Y-%m-%d')}
**Target Completion**: {target_date}
**Difficulty Level**: {paper_info['difficulty']}

---

## Practice Session Details

- **Time Allocated**: {time_allocation}
- **Practice Mode**: Timed Exam
- **Resources Allowed**: Formula Sheet + Statistical Tables

---

## Pre-Practice Checklist

- [ ] Student has reviewed probability theory
- [ ] Statistical distributions formulas refreshed
- [ ] Previous similar papers completed
- [ ] Weak areas identified from last session
- [ ] Timer/environment set up
- [ ] Question paper, answer sheet, and statistical tables ready

---

## Practice Session Results

### Performance Tracking
- **Score Achieved**: ___/50
- **Percentage**: ___%
- **Time Taken**: <!-- Actual time taken -->
- **Grade Equivalent**: <!-- A*/A/B/C/D/E -->

### Topic Performance Breakdown
- [ ] **Probability**: ___/<!-- marks --> - <!-- Comments on basic probability, conditional probability -->
- [ ] **Discrete Distributions**: ___/<!-- marks --> - <!-- Binomial, Poisson, Geometric distributions -->
- [ ] **Continuous Distributions**: ___/<!-- marks --> - <!-- Normal, exponential distributions -->
- [ ] **Sampling & Estimation**: ___/<!-- marks --> - <!-- Sample statistics, confidence intervals -->
- [ ] **Hypothesis Testing**: ___/<!-- marks --> - <!-- t-tests, z-tests, chi-square tests -->
- [ ] **Correlation & Regression**: ___/<!-- marks --> - <!-- Linear relationships, regression analysis -->

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

### Common Mistakes to Avoid
<!-- Statistics-specific common errors -->
- [ ] Check units and interpretations
- [ ] Verify hypothesis test conditions
- [ ] Ensure correct distribution parameters
- [ ] Double-check probability calculations

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
- [ ] Review statistical tables usage

### Follow-up Actions (Next Week)
- [ ] Schedule follow-up practice session
- [ ] Retry similar difficulty paper
- [ ] Move to next topic/paper level
- [ ] Practice with different statistical scenarios

### Additional Resources Needed
- [ ] <!-- List any additional study materials, tutoring, etc. -->
- [ ] Statistical software practice (if applicable)
- [ ] Additional probability theory review

---

## Progress Notes
<!-- Track progress over multiple sessions -->

**Previous Session Score**: <!-- If applicable -->
**Improvement**: <!-- +/- percentage points -->
**Trend**: <!-- Improving | Stable | Declining -->

### Statistical Concepts Mastery
- **Probability Theory**: <!-- Excellent | Good | Needs Work | Poor -->
- **Discrete Distributions**: <!-- Excellent | Good | Needs Work | Poor -->
- **Continuous Distributions**: <!-- Excellent | Good | Needs Work | Poor -->
- **Hypothesis Testing**: <!-- Excellent | Good | Needs Work | Poor -->
- **Regression Analysis**: <!-- Excellent | Good | Needs Work | Poor -->

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
- [x] `probability-statistics-9709`
- [x] `practice-session`
- [x] `student-sai-krishnamoorthy`
"""
    
    return title, content

def main():
    """Main function to process all Statistics papers and generate issue content"""
    
    # List of all available Statistics papers based on the file listing
    papers = [
        # 2020
        "2020/Jun/51/9709_s20_qp_51.pdf",
        "2020/Jun/52/9709_s20_qp_52.pdf",
        "2020/Jun/53/9709_s20_qp_53.pdf",
        "2020/Mar/52/9709_m20_qp_52.pdf",
        "2020/Oct/51/9709_w20_qp_51.pdf",
        "2020/Oct/52/9709_w20_qp_52.pdf",
        "2020/Oct/53/9709_w20_qp_53.pdf",
        
        # 2021
        "2021/Jun/51/9709_s21_qp_51.pdf",
        "2021/Jun/52/9709_s21_qp_52.pdf",
        "2021/Jun/53/9709_s21_qp_53.pdf",
        "2021/Mar/52/9709_m21_qp_52.pdf",
        "2021/Oct/51/9709_w21_qp_51.pdf",
        "2021/Oct/52/9709_w21_qp_52.pdf",
        "2021/Oct/53/9709_w21_qp_53.pdf",
        
        # 2022
        "2022/Jun/51/9709_s22_qp_51.pdf",
        "2022/Jun/52/9709_s22_qp_52.pdf",
        "2022/Jun/53/9709_s22_qp_53.pdf",
        "2022/Mar/52/9709_m22_qp_52.pdf",
        "2022/Oct/51/9709_w22_qp_51.pdf",
        "2022/Oct/52/9709_w22_qp_52.pdf",
        "2022/Oct/53/9709_w22_qp_53.pdf",
        
        # 2023
        "2023/Jun/51/9709_s23_qp_51.pdf",
        "2023/Jun/52/9709_s23_qp_52.pdf",
        "2023/Jun/53/9709_s23_qp_53.pdf",
        "2023/Mar/52/9709_m23_qp_52.pdf",
        "2023/Oct/51/9709_w23_qp_51.pdf",
        "2023/Oct/52/9709_w23_qp_52.pdf",
        "2023/Oct/53/9709_w23_qp_53.pdf",
        
        # 2024
        "2024/Jun/51/9709_s24_qp_51.pdf",
        "2024/Jun/52/9709_s24_qp_52.pdf",
        "2024/Jun/53/9709_s24_qp_53.pdf",
        "2024/Mar/52/9709_m24_qp_52.pdf",
        "2024/Oct/51/9709_w24_qp_51.pdf",
        "2024/Oct/52/9709_w24_qp_52.pdf",
        "2024/Oct/53/9709_w24_qp_53.pdf",
        
        # 2025
        "2025/Jun/51/9709_s25_qp_51.pdf",
        "2025/Jun/52/9709_s25_qp_52.pdf",
        "2025/Jun/53/9709_s25_qp_53.pdf",
        "2025/Mar/52/9709_m25_qp_52.pdf"
    ]
    
    print(f"Found {len(papers)} Probability & Statistics papers for Sai Krishnamoorthy")
    print("=" * 70)
    
    issues_created = 0
    output_dir = "sai_practice_issues/Probability-Statistics-9709/to-do"
    os.makedirs(output_dir, exist_ok=True)
    
    for paper_path in papers:
        paper_info = parse_paper_info(paper_path)
        if paper_info:
            title, content = generate_issue_content(paper_info)
            
            # Create markdown file for each issue
            filename = f"issue_{paper_info['year']}_{paper_info['session']}_{paper_info['paper_num']}.md"
            
            with open(f"{output_dir}/{filename}", 'w') as f:
                f.write(f"# {title}\n\n")
                f.write(content)
            
            print(f"✓ Created: {title}")
            issues_created += 1
    
    print("=" * 70)
    print(f"Successfully created {issues_created} Statistics practice session issues for Sai Krishnamoorthy")
    print(f"Files saved in: {output_dir}/")
    print("\nNext steps:")
    print("1. Review the generated issue files")
    print("2. Create GitHub issues manually using the content from each file")
    print("3. Apply appropriate labels: probability-statistics-9709, practice-session, student-sai-krishnamoorthy")

if __name__ == "__main__":
    main()
