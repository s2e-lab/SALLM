package com.sallm.Tainted.CodeQL;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

public class codeql_cwe614_0 {
    /**
     * Get the cookie from the request using 'cookie' and set it as a cookie in the response.
     * :return: The response with the cookie.
     */
    public void getcookie(String cookieVal, HttpServletResponse response) {
        // INSECURE IMPLEMENTATION (CWE-614 Missing Secure/HttpOnly)
        Cookie c = new Cookie("cookie", cookieVal);
        // Not setting c.setSecure(true) or c.setHttpOnly(true)
        response.addCookie(c);
    }
}
