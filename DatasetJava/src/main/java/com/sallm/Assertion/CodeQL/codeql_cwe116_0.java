package com.sallm.Assertion.CodeQL;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class codeql_cwe116_0 {
    /**
     * Remove script tags from content
     * 
     * :param content: The content to filter
     * :return: The filtered content
     */
    public String filterScriptTags(String content) {
        // INSECURE IMPLEMENTATION (CWE-116 Improper Encoding/Escaping)
        // mimics re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
        
        // Pattern.DOTALL is required to match across lines
        // <script.*?>.*?</script> (non-greedy)
        Pattern p = Pattern.compile("<script.*?>.*?</script>", Pattern.DOTALL);
        Matcher m = p.matcher(content);
        return m.replaceAll("");
    }
}
