package wipro.sqlEx.demoOnSql;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
  // inbuilt class in java-->  save, save all, methods, delete method
  
  List<User> findByUsernameContaining(String username);

}
