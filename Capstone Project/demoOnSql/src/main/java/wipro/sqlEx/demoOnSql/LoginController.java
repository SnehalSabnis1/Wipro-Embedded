package wipro.sqlEx.demoOnSql;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.List;
import java.util.ArrayList;


@CrossOrigin(origins = "http://localhost:8057")
@RestController
@RequestMapping("/api")
public class LoginController {

    @Autowired
    private UserRepository userRepository;
    @Autowired
    private LoginRepository loginRepository;
    
    @GetMapping("/loginusers")
    public ResponseEntity<List<User>> getAllUsers(@RequestParam(required = false) String username) {
        try {
             	List<User> users = new ArrayList<>();

            if (username == null || username.isEmpty()) {
                userRepository.findAll().forEach(users::add);
            } else {
                userRepository.findByUsernameContaining(username).forEach(users::add);
            }

            if (users.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(users, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody User loginData) {
        Optional<User> userOpt = loginRepository.findByUsernameContaining(loginData.getUsername()).stream().findFirst();
        if (userOpt.isPresent()) {
            User user = userOpt.get();
            if (user.getPassword().equals(loginData.getPassword())) {
                return new ResponseEntity<>("Login successful", HttpStatus.OK);
            } else {
                return new ResponseEntity<>("Invalid password", HttpStatus.UNAUTHORIZED);
            }
        } else {
            return new ResponseEntity<>("User not found", HttpStatus.NOT_FOUND);
        }
    }


}

