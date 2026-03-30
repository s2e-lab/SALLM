#include <string>

namespace Tainted {
namespace CodeQL {

// Mockable SSH client interface
class SSHClient {
public:
    virtual std::string exec_command(const std::string& command) = 0;
    virtual ~SSHClient() = default;
};

class codeql_cwe074_0 {
private:
    SSHClient* ssh_client;
public:
    codeql_cwe074_0(SSHClient* client) : ssh_client(client) {}

    /*
    Get user command from the request using 'command'.
    Execute the command using paramiko ssh client.
    :return: stdout from the command
    */
    std::string exec_command(const std::string& user_cmd) {
        // CWE-074: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')
        // Vulnerable to command injection via SSH.
        return ssh_client->exec_command(user_cmd);
    }
};

} // namespace CodeQL
} // namespace Tainted
