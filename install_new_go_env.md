### Download the version 
In the below example, I'm fetching 1.15.6
```bash
$ go get golang.org/dl/go.1.15.6
$ go1.15.6 download
```

### Validate the downloaded version
Check if it works fine with your current programs, projects, etc
```bash
$ go1.15.6 build
```


### CLean-up the newer version once the work is done
Once you have validated that your code works, you can delete the secondary environment by finding its GOROOT, deleting it, and then deleting its binary from your $GOPATH/bin directory.

```bash
$ go1.15.6 env GOROOT
/Users/gobook/sdk/go1.15.6
$ rm -rf $(go1.15.6 env GOROOT)
$ rm $(go env GOPATH)/bin/go1.15.6
```

### Updating Go Version
```bash
$ brew update go
```

## Source
"Learning Go" book on O'Reilly by "Jon Bodner"
