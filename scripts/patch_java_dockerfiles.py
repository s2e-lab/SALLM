import os
import glob

def patch_dockerfiles():
    # Find all Dockerfiles in the DatasetJava directory
    dockerfiles = glob.glob("DatasetJava/src/main/java/com/sallm/**/*_Dockerfile", recursive=True)
    
    print(f"Found {len(dockerfiles)} Dockerfiles to patch.")
    
    patched_count = 0
    for df_path in dockerfiles:
        with open(df_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        modified = False
        for line in lines:
            new_lines.append(line)
            # Add dependency:go-offline after COPY pom.xml .
            if 'COPY pom.xml .' in line and 'RUN mvn dependency:go-offline -B' not in "".join(lines):
                new_lines.append("RUN mvn dependency:go-offline -B\n")
                modified = True
        
        if modified:
            with open(df_path, 'w') as f:
                f.writelines(new_lines)
            patched_count += 1

    print(f"Patched {patched_count} Dockerfiles.")

if __name__ == "__main__":
    patch_dockerfiles()
