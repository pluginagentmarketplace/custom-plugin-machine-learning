---
name: linux-sysadmin
description: Master Linux for server management and system administration.
---

# Linux System Administration

## Essential Commands

### File Management
```bash
ls -la              # List files with details
cp source dest      # Copy files
mv source dest      # Move files
rm file            # Remove file
mkdir dirname      # Create directory
find . -name "*.log"  # Find files
```

### User Management
```bash
useradd username   # Create user
passwd username    # Set password
usermod -aG sudo username  # Add to group
userdel username   # Delete user
```

### Permissions
```bash
chmod 755 file     # Set permissions (rwxr-xr-x)
chown user:group file  # Change owner
chmod +x script.sh # Make executable
```

### System Information
```bash
uname -a          # System info
df -h             # Disk usage
ps aux            # Running processes
top               # Process monitor
```

## Package Management

```bash
apt update && apt upgrade    # Debian/Ubuntu
yum update && yum upgrade    # RedHat/CentOS
apt install package          # Install package
```

## Networking

```bash
ifconfig          # Network interfaces
netstat -tuln     # Listening ports
ss -tuln          # Modern netstat
ping host         # Test connectivity
ssh user@host     # Remote login
scp file user@host:/path  # Copy over SSH
```

## Best Practices

✅ Use sudo instead of root
✅ Regular backups
✅ Monitor logs
✅ Keep system updated
✅ Configure firewall
✅ Manage SSH keys
✅ Document changes

