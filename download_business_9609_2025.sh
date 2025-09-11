#!/bin/bash
# Business 9609 2025 Papers and Mark Schemes Download Script
# Downloads Cambridge International AS & A Level Business 9609 2025 papers from dynamicpapers.com

BASE_URL="https://dynamicpapers.com/wp-content/uploads/2015/09/"
SESSIONS=("w" "s" "m")
YEARS=("25")
PAPERS=("11" "12" "13" "21" "22" "23")

echo "=== Business 9609 2025 Papers & Mark Schemes Download Script ==="
echo "Downloading Cambridge International AS & A Level Business 2025 papers..."
echo ""

# Statistics
total_files=0
downloaded_files=0
existing_files=0
failed_downloads=0

for year in "${YEARS[@]}"; do
    for session in "${SESSIONS[@]}"; do
        for paper in "${PAPERS[@]}"; do
            # Skip March papers that don't exist (only 12, 22 available)
            if [[ "$session" == "m" && "$paper" != "12" && "$paper" != "22" ]]; then
                continue
            fi
            
            # Create directory structure
            if [[ "$session" == "w" ]]; then
                session_name="Oct"
            elif [[ "$session" == "s" ]]; then
                session_name="Jun"
            else
                session_name="Mar"
            fi
            
            dir="subjects/business-9609/20${year}/${session_name}/${paper}"
            mkdir -p "$dir"
            
            # Download both question paper and mark scheme
            for file_type in "qp" "ms"; do
                filename="9609_${session}${year}_${file_type}_${paper}.pdf"
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
echo "=== 2025 Download Summary ==="
echo "Total files processed: $total_files"
echo "Already existing: $existing_files"
echo "Successfully downloaded: $downloaded_files"
echo "Failed downloads: $failed_downloads"
echo ""

# Verify question papers and mark schemes are paired for 2025
echo "=== 2025 Verification: Question Papers vs Mark Schemes ==="
qp_2025_count=$(find subjects/business-9609/2025 -name "*qp*.pdf" 2>/dev/null | wc -l)
ms_2025_count=$(find subjects/business-9609/2025 -name "*ms*.pdf" 2>/dev/null | wc -l)
echo "2025 Question papers: $qp_2025_count"
echo "2025 Mark schemes: $ms_2025_count"

if [[ $qp_2025_count -eq $ms_2025_count ]]; then
    echo "✅ Perfect match: All 2025 question papers have corresponding mark schemes"
else
    echo "⚠ Mismatch detected: Some 2025 mark schemes may be missing"
fi

echo ""
echo "=== Complete Business 9609 Collection Status ==="
total_qp=$(find subjects/business-9609 -name "*qp*.pdf" | wc -l)
total_ms=$(find subjects/business-9609 -name "*ms*.pdf" | wc -l)
total_files_all=$(find subjects/business-9609 -name "*.pdf" | wc -l)

echo "Total Question papers: $total_qp"
echo "Total Mark schemes: $total_ms"
echo "Total PDF files: $total_files_all"

if [[ $total_qp -eq $total_ms ]]; then
    echo "✅ Perfect collection: All question papers have corresponding mark schemes"
else
    echo "⚠ Collection status: $((total_qp - total_ms)) papers without mark schemes"
fi

echo ""
echo "=== Years Coverage ==="
find subjects/business-9609 -maxdepth 1 -type d -name "20*" | sort | while read year_dir; do
    year=$(basename "$year_dir")
    qp_count=$(find "$year_dir" -name "*qp*.pdf" | wc -l)
    ms_count=$(find "$year_dir" -name "*ms*.pdf" | wc -l)
    echo "$year: $qp_count papers + $ms_count mark schemes"
done

echo ""
echo "=== Next Steps ==="
echo "1. Verify 2025 paper completeness"
echo "2. Update repository documentation"
echo "3. Begin processing 2025 papers using 6-step methodology"
echo "4. Create comprehensive answer solutions with mark scheme validation"
echo ""
echo "Business 9609 2025 expansion complete!"
