## One Poetry

**Author:** feiwangoooh  
**Version:** 0.0.1  
**Type:** Tool 



### Description

Randomly returns a famous line from classical Chinese poetry.  

### Plugin Description

This is a Dify plugin developed based on the [GuShiCi·YiYanAPI](http://gushi.ci/), which can randomly return a famous line from classical Chinese poetry. The plugin requires no credentials or additional configuration. Simply call the tool to receive a random classical poetry line along with its author and source information.  

### Features

- Randomly returns a famous line from classical Chinese poetry
- Automatically includes author and source information
- No credentials or additional configuration required
- Built based on the ** Dify ** plugin framework  

### Usage Screenshots

<img src="images/1.png" width="1056" height="210">  
<img src="images/2.png" width="1295" height="713">  

### Implementation Details

The plugin works by sending requests to the [GuShiCi·YIYanAPI](https://v1.jinrishici.com/all.json) and formatting the response. The returned content includes:  
- The poetry line
- Author information
- Original work source  

Implemented in the [tools/one_poetry.py](tools/one_poetry.py) file using Python and the requests library.  

### Repository Address

https://github.com/feiwangoooh/one_poetry/  

### Contact Information

2272142334@qq.com  

### Acknowledgments

Special thanks to the author of the [GuShiCi·YIYanAPI](http://gushi.ci/) for their contribution to Chinese traditional culture.