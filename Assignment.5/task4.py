"""
Job Applicant Scoring System
This system evaluates and scores job applicants based on multiple features
including education, experience, skills, certifications, and other qualifications.
"""

import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from collections import defaultdict

# Scoring weights for different features (can be customized)
SCORING_WEIGHTS = {
    "education": 0.25,      # 25% weight
    "experience": 0.30,     # 30% weight
    "skills": 0.20,         # 20% weight
    "certifications": 0.10, # 10% weight
    "interview": 0.10,      # 10% weight
    "references": 0.05      # 5% weight
}

# Education level scores (out of 100)
EDUCATION_SCORES = {
    "high_school": 40,
    "associate": 60,
    "bachelor": 80,
    "master": 90,
    "phd": 100,
    "professional": 95
}

# Experience level scores (years of experience mapped to score)
def calculate_experience_score(years: float) -> float:
    """Calculate experience score based on years of experience"""
    if years < 0:
        return 0
    elif years < 1:
        return 30
    elif years < 2:
        return 50
    elif years < 5:
        return 70
    elif years < 10:
        return 85
    else:
        return 100

# Skill proficiency levels
SKILL_LEVELS = {
    "beginner": 30,
    "intermediate": 60,
    "advanced": 85,
    "expert": 100
}

# Interview performance scores
INTERVIEW_SCORES = {
    "poor": 30,
    "fair": 50,
    "good": 70,
    "very_good": 85,
    "excellent": 100
}

# Reference quality scores
REFERENCE_SCORES = {
    "poor": 30,
    "fair": 50,
    "good": 70,
    "very_good": 85,
    "excellent": 100
}

def calculate_education_score(education_level: str, relevant_field: bool = True) -> float:
    """
    Calculate education score based on education level and field relevance
    
    Args:
        education_level: Level of education (high_school, associate, bachelor, etc.)
        relevant_field: Whether the education is in a relevant field
    
    Returns:
        float: Education score (0-100)
    """
    base_score = EDUCATION_SCORES.get(education_level.lower(), 0)
    
    # Bonus for relevant field
    if relevant_field and base_score > 0:
        return min(100, base_score + 5)
    
    return base_score

def calculate_skills_score(skills: List[Dict[str, str]], required_skills: List[str] = None) -> float:
    """
    Calculate skills score based on skill proficiency levels
    
    Args:
        skills: List of dictionaries with 'name' and 'level' keys
        required_skills: List of required skill names (optional)
    
    Returns:
        float: Skills score (0-100)
    """
    if not skills:
        return 0
    
    total_score = 0
    skill_count = len(skills)
    
    # Calculate average skill proficiency
    for skill in skills:
        level = skill.get("level", "beginner").lower()
        score = SKILL_LEVELS.get(level, 0)
        total_score += score
    
    average_score = total_score / skill_count if skill_count > 0 else 0
    
    # Bonus for having required skills
    if required_skills:
        required_count = 0
        for skill in skills:
            if skill.get("name", "").lower() in [s.lower() for s in required_skills]:
                required_count += 1
        
        if required_count > 0:
            coverage_bonus = (required_count / len(required_skills)) * 20
            average_score = min(100, average_score + coverage_bonus)
    
    return average_score

def calculate_certifications_score(certifications: List[Dict[str, str]], 
                                   required_certs: List[str] = None) -> float:
    """
    Calculate certifications score
    
    Args:
        certifications: List of certification dictionaries with 'name' and 'valid' keys
        required_certs: List of required certification names (optional)
    
    Returns:
        float: Certifications score (0-100)
    """
    if not certifications:
        return 0
    
    valid_count = sum(1 for cert in certifications if cert.get("valid", True))
    total_count = len(certifications)
    
    base_score = (valid_count / total_count) * 100 if total_count > 0 else 0
    
    # Bonus for having required certifications
    if required_certs:
        required_count = 0
        for cert in certifications:
            if cert.get("name", "").lower() in [c.lower() for c in required_certs]:
                required_count += 1
        
        if required_count > 0:
            coverage_bonus = (required_count / len(required_certs)) * 30
            base_score = min(100, base_score + coverage_bonus)
    
    return base_score

def calculate_interview_score(interview_performance: str) -> float:
    """Calculate interview score based on performance rating"""
    return INTERVIEW_SCORES.get(interview_performance.lower(), 0)

def calculate_references_score(reference_quality: str) -> float:
    """Calculate references score based on quality rating"""
    return REFERENCE_SCORES.get(reference_quality.lower(), 0)

def calculate_total_score(applicant: Dict, weights: Dict = None) -> Tuple[float, Dict]:
    """
    Calculate total weighted score for an applicant
    
    Args:
        applicant: Dictionary containing applicant information
        weights: Optional custom weights dictionary
    
    Returns:
        Tuple of (total_score, score_breakdown)
    """
    if weights is None:
        weights = SCORING_WEIGHTS
    
    # Calculate individual component scores
    education_score = calculate_education_score(
        applicant.get("education_level", ""),
        applicant.get("education_relevant", True)
    )
    
    experience_years = applicant.get("experience_years", 0)
    experience_score = calculate_experience_score(experience_years)
    
    skills_score = calculate_skills_score(
        applicant.get("skills", []),
        applicant.get("required_skills", None)
    )
    
    certifications_score = calculate_certifications_score(
        applicant.get("certifications", []),
        applicant.get("required_certifications", None)
    )
    
    interview_score = calculate_interview_score(
        applicant.get("interview_performance", "fair")
    )
    
    references_score = calculate_references_score(
        applicant.get("reference_quality", "fair")
    )
    
    # Calculate weighted total score
    total_score = (
        education_score * weights.get("education", 0.25) +
        experience_score * weights.get("experience", 0.30) +
        skills_score * weights.get("skills", 0.20) +
        certifications_score * weights.get("certifications", 0.10) +
        interview_score * weights.get("interview", 0.10) +
        references_score * weights.get("references", 0.05)
    )
    
    score_breakdown = {
        "education": education_score,
        "experience": experience_score,
        "skills": skills_score,
        "certifications": certifications_score,
        "interview": interview_score,
        "references": references_score,
        "total": total_score
    }
    
    return total_score, score_breakdown

def get_education_level() -> Optional[str]:
    """Menu-driven education level selection"""
    print("\n" + "-" * 50)
    print("SELECT EDUCATION LEVEL:")
    print("-" * 50)
    print("1. High School")
    print("2. Associate Degree")
    print("3. Bachelor's Degree")
    print("4. Master's Degree")
    print("5. PhD")
    print("6. Professional Degree")
    print("0. Cancel")
    print("-" * 50)
    
    choice = input("Enter your choice (1-6, 0 to cancel): ").strip()
    
    education_map = {
        "1": "high_school",
        "2": "associate",
        "3": "bachelor",
        "4": "master",
        "5": "phd",
        "6": "professional"
    }
    
    if choice == "0":
        return None
    elif choice in education_map:
        return education_map[choice]
    else:
        print(f"[ERROR] Invalid choice '{choice}'. Please try again.")
        return get_education_level()

def get_skill_level() -> Optional[str]:
    """Menu-driven skill level selection"""
    print("\n" + "-" * 50)
    print("SELECT SKILL LEVEL:")
    print("-" * 50)
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    print("4. Expert")
    print("0. Cancel")
    print("-" * 50)
    
    choice = input("Enter your choice (1-4, 0 to cancel): ").strip()
    
    level_map = {
        "1": "beginner",
        "2": "intermediate",
        "3": "advanced",
        "4": "expert"
    }
    
    if choice == "0":
        return None
    elif choice in level_map:
        return level_map[choice]
    else:
        print(f"[ERROR] Invalid choice '{choice}'. Please try again.")
        return get_skill_level()

def get_performance_rating() -> Optional[str]:
    """Menu-driven performance rating selection"""
    print("\n" + "-" * 50)
    print("SELECT PERFORMANCE RATING:")
    print("-" * 50)
    print("1. Poor")
    print("2. Fair")
    print("3. Good")
    print("4. Very Good")
    print("5. Excellent")
    print("0. Cancel")
    print("-" * 50)
    
    choice = input("Enter your choice (1-5, 0 to cancel): ").strip()
    
    rating_map = {
        "1": "poor",
        "2": "fair",
        "3": "good",
        "4": "very_good",
        "5": "excellent"
    }
    
    if choice == "0":
        return None
    elif choice in rating_map:
        return rating_map[choice]
    else:
        print(f"[ERROR] Invalid choice '{choice}'. Please try again.")
        return get_performance_rating()

def get_skills_from_keyboard() -> List[Dict[str, str]]:
    """Get skills information from keyboard input"""
    skills = []
    print("\n--- Skills Information ---")
    print("Enter skills (press Enter with empty name to finish)")
    
    while True:
        skill_name = input("Enter skill name (or press Enter to finish): ").strip()
        if not skill_name:
            break
        
        skill_level = get_skill_level()
        if skill_level is None:
            continue
        
        skills.append({
            "name": skill_name,
            "level": skill_level
        })
        print(f"[OK] Added skill: {skill_name} ({skill_level})")
    
    return skills

def get_certifications_from_keyboard() -> List[Dict[str, str]]:
    """Get certifications information from keyboard input"""
    certifications = []
    print("\n--- Certifications Information ---")
    print("Enter certifications (press Enter with empty name to finish)")
    
    while True:
        cert_name = input("Enter certification name (or press Enter to finish): ").strip()
        if not cert_name:
            break
        
        valid_input = input("Is this certification valid? (y/n) [default: y]: ").strip().lower()
        is_valid = valid_input != 'n'
        
        certifications.append({
            "name": cert_name,
            "valid": is_valid
        })
        status = "valid" if is_valid else "invalid"
        print(f"[OK] Added certification: {cert_name} ({status})")
    
    return certifications

def get_applicant_from_keyboard() -> Optional[Dict]:
    """Get applicant information using menu-driven selection"""
    print("\n" + "=" * 70)
    print("ENTER APPLICANT INFORMATION")
    print("=" * 70)
    print("(Press 0 to cancel and finish adding applicants)\n")
    
    # Basic information
    name = input("Enter applicant name: ").strip()
    if not name:
        return None
    
    email = input("Enter email (optional): ").strip()
    position = input("Enter position applied for: ").strip()
    
    # Education
    print("\n--- Education Information ---")
    education_level = get_education_level()
    if education_level is None:
        return None
    
    relevant_input = input("Is education in relevant field? (y/n) [default: y]: ").strip().lower()
    education_relevant = relevant_input != 'n'
    
    # Experience
    print("\n--- Experience Information ---")
    try:
        experience_years = float(input("Enter years of experience: ").strip())
    except ValueError:
        print("[ERROR] Invalid input. Using 0 years.")
        experience_years = 0
    
    # Skills
    skills = get_skills_from_keyboard()
    
    # Certifications
    certifications = get_certifications_from_keyboard()
    
    # Interview performance
    print("\n--- Interview Performance ---")
    interview_performance = get_performance_rating()
    if interview_performance is None:
        interview_performance = "fair"
    
    # References
    print("\n--- Reference Quality ---")
    reference_quality = get_performance_rating()
    if reference_quality is None:
        reference_quality = "fair"
    
    applicant = {
        "name": name,
        "email": email if email else None,
        "position": position,
        "education_level": education_level,
        "education_relevant": education_relevant,
        "experience_years": experience_years,
        "skills": skills,
        "certifications": certifications,
        "interview_performance": interview_performance,
        "reference_quality": reference_quality,
        "date_added": datetime.now().isoformat()
    }
    
    print(f"\n[OK] Applicant added: {name}")
    return applicant

def score_applicants(applicants: List[Dict], weights: Dict = None) -> List[Dict]:
    """
    Score all applicants and return sorted list by total score
    
    Args:
        applicants: List of applicant dictionaries
        weights: Optional custom weights dictionary
    
    Returns:
        List of applicants with scores, sorted by total score (descending)
    """
    scored_applicants = []
    
    for applicant in applicants:
        total_score, score_breakdown = calculate_total_score(applicant, weights)
        
        scored_applicant = {
            **applicant,
            "score": total_score,
            "score_breakdown": score_breakdown
        }
        scored_applicants.append(scored_applicant)
    
    # Sort by total score (descending)
    scored_applicants.sort(key=lambda x: x["score"], reverse=True)
    
    return scored_applicants

def display_applicant_scores(applicants: List[Dict]):
    """Display scores for all applicants"""
    print("\n" + "=" * 100)
    print("APPLICANT SCORING RESULTS")
    print("=" * 100)
    
    if not applicants:
        print("\n[INFO] No applicants to display.")
        return
    
    print(f"\nTotal Applicants: {len(applicants)}\n")
    print("-" * 100)
    print(f"{'Rank':<6} {'Name':<25} {'Total Score':<12} {'Education':<12} {'Experience':<12} {'Skills':<12} {'Position':<20}")
    print("-" * 100)
    
    for rank, applicant in enumerate(applicants, 1):
        name = applicant.get("name", "Unknown")
        score = applicant.get("score", 0)
        breakdown = applicant.get("score_breakdown", {})
        position = applicant.get("position", "N/A")
        
        education = breakdown.get("education", 0)
        experience = breakdown.get("experience", 0)
        skills = breakdown.get("skills", 0)
        
        print(f"{rank:<6} {name:<25} {score:>10.2f}  {education:>10.2f}  {experience:>10.2f}  {skills:>10.2f}  {position:<20}")
    
    print("-" * 100)

def display_detailed_applicant(applicant: Dict):
    """Display detailed information for a single applicant"""
    print("\n" + "=" * 100)
    print(f"DETAILED APPLICANT INFORMATION: {applicant.get('name', 'Unknown')}")
    print("=" * 100)
    
    print(f"\nName: {applicant.get('name', 'N/A')}")
    if applicant.get('email'):
        print(f"Email: {applicant.get('email')}")
    print(f"Position: {applicant.get('position', 'N/A')}")
    
    print(f"\n--- SCORES ---")
    breakdown = applicant.get("score_breakdown", {})
    total_score = applicant.get("score", 0)
    
    print(f"Total Score: {total_score:.2f}/100")
    print(f"  Education: {breakdown.get('education', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['education']*100:.0f}%)")
    print(f"  Experience: {breakdown.get('experience', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['experience']*100:.0f}%)")
    print(f"  Skills: {breakdown.get('skills', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['skills']*100:.0f}%)")
    print(f"  Certifications: {breakdown.get('certifications', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['certifications']*100:.0f}%)")
    print(f"  Interview: {breakdown.get('interview', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['interview']*100:.0f}%)")
    print(f"  References: {breakdown.get('references', 0):.2f}/100 (Weight: {SCORING_WEIGHTS['references']*100:.0f}%)")
    
    print(f"\n--- QUALIFICATIONS ---")
    print(f"Education Level: {applicant.get('education_level', 'N/A').replace('_', ' ').title()}")
    print(f"Education Relevant: {'Yes' if applicant.get('education_relevant', False) else 'No'}")
    print(f"Experience Years: {applicant.get('experience_years', 0)}")
    
    print(f"\nSkills:")
    skills = applicant.get('skills', [])
    if skills:
        for skill in skills:
            print(f"  - {skill.get('name', 'N/A')}: {skill.get('level', 'N/A').title()}")
    else:
        print("  None")
    
    print(f"\nCertifications:")
    certifications = applicant.get('certifications', [])
    if certifications:
        for cert in certifications:
            status = "Valid" if cert.get('valid', True) else "Invalid"
            print(f"  - {cert.get('name', 'N/A')}: {status}")
    else:
        print("  None")
    
    print(f"\nInterview Performance: {applicant.get('interview_performance', 'N/A').replace('_', ' ').title()}")
    print(f"Reference Quality: {applicant.get('reference_quality', 'N/A').replace('_', ' ').title()}")
    
    print("=" * 100)

def save_results_to_file(applicants: List[Dict], filename: str = "applicant_scores.json"):
    """Save scoring results to JSON file"""
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_applicants": len(applicants),
        "scoring_weights": SCORING_WEIGHTS,
        "applicants": applicants
    }
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n[SAVED] Results saved to {filename}")

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 70)
    print("        JOB APPLICANT SCORING SYSTEM")
    print("=" * 70)
    print("1. Add Applicant")
    print("2. Score All Applicants")
    print("3. Display Scores Summary")
    print("4. Display Detailed Applicant Information")
    print("5. Save Results to File")
    print("6. Load Applicants from File")
    print("7. Clear All Applicants")
    print("8. Exit")
    print("=" * 70)

def main():
    """Main function to run the scoring system"""
    applicants = []
    scored_applicants = []
    
    print("\n" + "=" * 70)
    print("WELCOME TO JOB APPLICANT SCORING SYSTEM")
    print("=" * 70)
    print("\nThis system evaluates job applicants based on multiple features:")
    print("  - Education Level and Relevance")
    print("  - Years of Experience")
    print("  - Skills and Proficiency Levels")
    print("  - Certifications")
    print("  - Interview Performance")
    print("  - Reference Quality")
    print("\nApplicants are scored using weighted criteria and ranked accordingly.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":  # Add Applicant
            print("\n--- ADD APPLICANT ---")
            applicant = get_applicant_from_keyboard()
            if applicant:
                applicants.append(applicant)
                scored_applicants = []  # Reset scored list
                print(f"\n[OK] Total applicants: {len(applicants)}")
        
        elif choice == "2":  # Score All Applicants
            print("\n--- SCORE ALL APPLICANTS ---")
            if not applicants:
                print("[ERROR] No applicants to score. Please add applicants first.")
            else:
                scored_applicants = score_applicants(applicants)
                print(f"\n[OK] Scored {len(scored_applicants)} applicants.")
                display_applicant_scores(scored_applicants)
        
        elif choice == "3":  # Display Scores Summary
            print("\n--- SCORES SUMMARY ---")
            if not scored_applicants:
                print("[INFO] No scored applicants. Please score applicants first (option 2).")
            else:
                display_applicant_scores(scored_applicants)
        
        elif choice == "4":  # Display Detailed Applicant
            print("\n--- DETAILED APPLICANT INFORMATION ---")
            if not scored_applicants:
                print("[INFO] No scored applicants. Please score applicants first (option 2).")
            else:
                display_applicant_scores(scored_applicants)
                try:
                    rank = int(input("\nEnter rank number to view details (or 0 to cancel): ").strip())
                    if rank == 0:
                        continue
                    elif 1 <= rank <= len(scored_applicants):
                        display_detailed_applicant(scored_applicants[rank - 1])
                    else:
                        print(f"[ERROR] Invalid rank. Please enter a number between 1 and {len(scored_applicants)}.")
                except ValueError:
                    print("[ERROR] Invalid input. Please enter a number.")
        
        elif choice == "5":  # Save Results
            print("\n--- SAVE RESULTS ---")
            if not scored_applicants:
                print("[WARNING] No scored applicants. Scoring applicants first...")
                scored_applicants = score_applicants(applicants)
            
            filename = input("Enter filename (default: applicant_scores.json): ").strip()
            if not filename:
                filename = "applicant_scores.json"
            
            if not filename.endswith('.json'):
                filename += '.json'
            
            save_results_to_file(scored_applicants, filename)
        
        elif choice == "6":  # Load from File
            print("\n--- LOAD APPLICANTS FROM FILE ---")
            filename = input("Enter filename to load: ").strip()
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        applicants = data
                    elif isinstance(data, dict) and "applicants" in data:
                        applicants = data["applicants"]
                    else:
                        print("[ERROR] Invalid file format.")
                        continue
                
                scored_applicants = []  # Reset scored list
                print(f"[OK] Loaded {len(applicants)} applicants from {filename}.")
            except FileNotFoundError:
                print(f"[ERROR] File '{filename}' not found.")
            except json.JSONDecodeError:
                print(f"[ERROR] Invalid JSON file: '{filename}'.")
            except Exception as e:
                print(f"[ERROR] Error loading file: {e}")
        
        elif choice == "7":  # Clear All
            print("\n--- CLEAR ALL APPLICANTS ---")
            confirm = input("Are you sure you want to clear all applicants? (y/n): ").strip().lower()
            if confirm == 'y':
                applicants = []
                scored_applicants = []
                print("[OK] All applicants cleared.")
            else:
                print("[CANCELLED] Operation cancelled.")
        
        elif choice == "8":  # Exit
            print("\n--- EXIT ---")
            if applicants:
                save_choice = input("Do you want to save results before exiting? (y/n): ").strip().lower()
                if save_choice == 'y':
                    if not scored_applicants:
                        scored_applicants = score_applicants(applicants)
                    save_results_to_file(scored_applicants)
            
            print("Thank you for using the Job Applicant Scoring System. Goodbye!")
            break
        
        else:
            print("\n[ERROR] Invalid choice! Please enter a number between 1-8.")

if __name__ == "__main__":
    main()

