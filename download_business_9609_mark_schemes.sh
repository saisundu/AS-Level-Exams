#!/bin/bash
# Business 9609 Mark Scheme Download Script
# Downloads Cambridge International AS & A Level Business 9609 mark schemes from dynamicpapers.com

BASE_URL="https://dynamicpapers.com/wp-content/uploads/2015/09/"
SESSIONS=("w" "s" "m")
YEARS=("20" "21" "22" "23" "24")
PAPERS=("11" "12" "13" "21" "22" "23")

echo "=== Business 9609 Mark Scheme Download Script ==="
echo "Downloading Cambridge International AS & A Level Business mark schemes..."
echo ""

# Statistics
total_schemes=0
downloaded_schemes=0
existing_schemes=0
failed_downloads=0

for year in "${YEARS[@]}"; do
    for session in "${SESSIONS[@]}"; do
        for paper in "${PAPERS[@]}"; do
            # Skip March papers that don't exist (only 12, 22 available)
            if [[ "$session" == "m" && "$paper" != "12" && "$paper" != "22" ]]; then
                continue
            fi
            
            filename="9609_${session}${year}_ms_${paper}.pdf"
            url="${BASE_URL}${filename}"
            
            # Create directory structure
            if [[ "$session" == "w" ]]; then
                session_name="Oct"
            elif [[ "$session" == "s" ]]; then
                session_name="Jun"
            else
                session_name="Mar"
            fi
            
            dir="subjects/business-9609/20${year}/${session_name}/${paper}"
            filepath="${dir}/${filename}"
            total_schemes=$((total_schemes + 1))
            
            # Check if directory exists (should exist from question paper download)
            if [[ ! -d "$dir" ]]; then
                echo "⚠ Directory missing: $dir (skipping)"
                continue
            fi
            
            # Check if file already exists
            if [[ -f "$filepath" ]]; then
                echo "✓ Already exists: ${filename}"
                existing_schemes=$((existing_schemes + 1))
                continue
            fi
            
            # Download the mark scheme
            echo "⬇ Downloading: ${filename}..."
            if curl -f -s -o "$filepath" "$url"; then
                # Verify the download (check if file size > 1KB)
                if [[ -f "$filepath" && $(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath" 2>/dev/null) -gt 1024 ]]; then
                    echo "✓ Downloaded: ${filename}"
                    downloaded_schemes=$((downloaded_schemes + 1))
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
            sleep 0.5
        done
    done
done

echo ""
echo "=== Mark Scheme Download Summary ==="
echo "Total mark schemes processed: $total_schemes"
echo "Already existing: $existing_schemes"
echo "Successfully downloaded: $downloaded_schemes"
echo "Failed downloads: $failed_downloads"
echo ""

# Verify question papers and mark schemes are paired
echo "=== Verification: Question Papers vs Mark Schemes ==="
qp_count=$(find subjects/business-9609 -name "*qp*.pdf" | wc -l)
ms_count=$(find subjects/business-9609 -name "*ms*.pdf" | wc -l)
echo "Question papers: $qp_count"
echo "Mark schemes: $ms_count"

if [[ $qp_count -eq $ms_count ]]; then
    echo "✅ Perfect match: All question papers have corresponding mark schemes"
else
    echo "⚠ Mismatch detected: Some mark schemes may be missing"
    echo ""
    echo "=== Missing Mark Schemes Analysis ==="
    
    # Find question papers without corresponding mark schemes
    for qp_file in $(find subjects/business-9609 -name "*qp*.pdf"); do
        # Extract the base name and convert qp to ms
        ms_file="${qp_file/qp/ms}"
        if [[ ! -f "$ms_file" ]]; then
            echo "Missing: $(basename "$ms_file")"
        fi
    done
fi

echo ""
echo "=== File Structure Overview ==="
echo "Business 9609 collection now includes:"
find subjects/business-9609 -name "*.pdf" | wc -l | xargs echo "Total PDF files:"
find subjects/business-9609 -name "*qp*.pdf" | wc -l | xargs echo "Question papers:"
find subjects/business-9609 -name "*ms*.pdf" | wc -l | xargs echo "Mark schemes:"

echo ""
echo "=== Next Steps ==="
echo "1. Verify mark scheme completeness"
echo "2. Begin processing papers using 6-step methodology"
echo "3. Create comprehensive answer solutions with mark scheme validation"
echo "4. Generate processing summaries for each paper"
echo ""
echo "Business 9609 mark scheme download complete!"
