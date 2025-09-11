#!/bin/bash
# Business 9609 Paper Download Script
# Downloads Cambridge International AS & A Level Business 9609 papers from dynamicpapers.com

BASE_URL="https://dynamicpapers.com/wp-content/uploads/2015/09/"
SESSIONS=("w" "s" "m")
YEARS=("20" "21" "22" "23" "24")
PAPERS=("11" "12" "13" "21" "22" "23")

echo "=== Business 9609 Paper Download Script ==="
echo "Downloading Cambridge International AS & A Level Business papers..."
echo ""

# Create base directory if it doesn't exist
mkdir -p subjects/business-9609

# Statistics
total_papers=0
downloaded_papers=0
existing_papers=0
failed_downloads=0

for year in "${YEARS[@]}"; do
    for session in "${SESSIONS[@]}"; do
        for paper in "${PAPERS[@]}"; do
            # Skip March papers that don't exist (only 12, 22 available)
            if [[ "$session" == "m" && "$paper" != "12" && "$paper" != "22" ]]; then
                continue
            fi
            
            filename="9609_${session}${year}_qp_${paper}.pdf"
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
            mkdir -p "$dir"
            
            filepath="${dir}/${filename}"
            total_papers=$((total_papers + 1))
            
            # Check if file already exists
            if [[ -f "$filepath" ]]; then
                echo "✓ Already exists: ${filename}"
                existing_papers=$((existing_papers + 1))
                continue
            fi
            
            # Download the file
            echo "⬇ Downloading: ${filename}..."
            if curl -f -s -o "$filepath" "$url"; then
                # Verify the download (check if file size > 1KB)
                if [[ -f "$filepath" && $(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath" 2>/dev/null) -gt 1024 ]]; then
                    echo "✓ Downloaded: ${filename}"
                    downloaded_papers=$((downloaded_papers + 1))
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
echo "=== Download Summary ==="
echo "Total papers processed: $total_papers"
echo "Already existing: $existing_papers"
echo "Successfully downloaded: $downloaded_papers"
echo "Failed downloads: $failed_downloads"
echo ""

# Create directory structure overview
echo "=== Directory Structure Created ==="
find subjects/business-9609 -type d | sort

echo ""
echo "=== Next Steps ==="
echo "1. Review downloaded papers for completeness"
echo "2. Begin processing papers using 6-step methodology"
echo "3. Create comprehensive answer solutions"
echo "4. Validate against Cambridge mark schemes"
echo ""
echo "Business 9609 expansion complete!"
