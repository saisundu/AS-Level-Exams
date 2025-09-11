#!/bin/bash
# Economics 9708 Paper 2 Download Script
# Downloads Cambridge International AS & A Level Economics 9708 Paper 2 from dynamicpapers.com

BASE_URL="https://dynamicpapers.com/wp-content/uploads/2015/09/"
SESSIONS=("w" "s" "m")
YEARS=("20" "21" "22" "23" "24" "25")
PAPERS=("22")  # Only Paper 2 variant 2

echo "=== Economics 9708 Paper 2 Download Script ==="
echo "Downloading Cambridge International AS & A Level Economics Paper 2..."
echo ""

# Create base directory
mkdir -p subjects/economics-9708

# Statistics
total_files=0
downloaded_files=0
existing_files=0
failed_downloads=0

for year in "${YEARS[@]}"; do
    for session in "${SESSIONS[@]}"; do
        for paper in "${PAPERS[@]}"; do
            # Create directory structure
            if [[ "$session" == "w" ]]; then
                session_name="Oct"
            elif [[ "$session" == "s" ]]; then
                session_name="Jun"
            else
                session_name="Mar"
            fi
            
            dir="subjects/economics-9708/20${year}/${session_name}/${paper}"
            mkdir -p "$dir"
            
            # Download both question paper and mark scheme
            for file_type in "qp" "ms"; do
                filename="9708_${session}${year}_${file_type}_${paper}.pdf"
                url="${BASE_URL}${filename}"
                filepath="${dir}/${filename}"
                total_files=$((total_files + 1))
                
                # Check if file already exists
                if [[ -f "$filepath" ]]; then
                    echo "✓ Already exists: ${filename}"
                    existing_files=$((existing_files + 1))
                    continue
                fi
                
                # Download the file
                echo "⬇ Downloading: ${filename}..."
                if curl -f -s -o "$filepath" "$url"; then
                    # Verify the download (check if file size > 1KB)
                    if [[ -f "$filepath" && $(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath" 2>/dev/null) -gt 1024 ]]; then
                        echo "✓ Downloaded: ${filename}"
                        downloaded_files=$((downloaded_files + 1))
                    else
                        echo "✗ Failed: ${filename} (invalid file)"
                        rm -f "$filepath"
                        failed_downloads=$((failed_downloads + 1))
                    fi
                else
                    echo "✗ Failed: ${filename} (download error)"
                    rm -f "$filepath"
                    failed_downloads=$((failed_downloads + 1))
                fi
                
                # Small delay to be respectful to the server
                sleep 0.3
            done
        done
    done
done

echo ""
echo "=== Economics 9708 Download Summary ==="
echo "Total files processed: $total_files"
echo "Already existing: $existing_files"
echo "Successfully downloaded: $downloaded_files"
echo "Failed downloads: $failed_downloads"
echo ""

# Verify question papers and mark schemes are paired
echo "=== Verification: Question Papers vs Mark Schemes ==="
qp_count=$(find subjects/economics-9708 -name "*qp*.pdf" | wc -l)
ms_count=$(find subjects/economics-9708 -name "*ms*.pdf" | wc -l)
echo "Question papers: $qp_count"
echo "Mark schemes: $ms_count"

if [[ $qp_count -eq $ms_count ]]; then
    echo "✅ Perfect match: All question papers have corresponding mark schemes"
else
    echo "⚠ Mismatch detected: Some mark schemes may be missing"
    echo ""
    echo "=== Missing Mark Schemes Analysis ==="
    
    # Find question papers without corresponding mark schemes
    for qp_file in $(find subjects/economics-9708 -name "*qp*.pdf"); do
        # Extract the base name and convert qp to ms
        ms_file="${qp_file/qp/ms}"
        if [[ ! -f "$ms_file" ]]; then
            echo "Missing: $(basename "$ms_file")"
        fi
    done
fi

echo ""
echo "=== Economics 9708 Collection Structure ==="
echo "Years Coverage:"
find subjects/economics-9708 -maxdepth 1 -type d -name "20*" | sort | while read year_dir; do
    year=$(basename "$year_dir")
    qp_count=$(find "$year_dir" -name "*qp*.pdf" | wc -l)
    ms_count=$(find "$year_dir" -name "*ms*.pdf" | wc -l)
    echo "$year: $qp_count papers + $ms_count mark schemes"
done

echo ""
echo "=== Directory Structure Created ==="
find subjects/economics-9708 -type d | sort

echo ""
echo "=== Economics Paper 2 Information ==="
echo "Paper 2: Data Response and Essay Questions"
echo "Duration: 2 hours 15 minutes"
echo "Marks: 40"
echo "Format: Section A (Data Response) + Section B (Essay Questions)"
echo "Topics: Microeconomics and Macroeconomics"

echo ""
echo "=== Repository Status Update ==="
total_subjects=$(find subjects -maxdepth 1 -type d -name "*-*" | wc -l)
total_pdf_files=$(find subjects -name "*.pdf" | wc -l)
echo "Total subjects in repository: $total_subjects"
echo "Total PDF files in repository: $total_pdf_files"

echo ""
echo "=== Next Steps ==="
echo "1. Update repository documentation to include Economics 9708"
echo "2. Create Economics processing plan using 6-step methodology"
echo "3. Begin processing papers with comprehensive answer solutions"
echo "4. Validate against Cambridge mark schemes"
echo ""
echo "Economics 9708 Paper 2 collection complete!"
