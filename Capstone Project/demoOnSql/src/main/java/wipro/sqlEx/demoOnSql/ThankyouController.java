package wipro.sqlEx.demoOnSql;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ThankyouController {
	@GetMapping("/thankyou")
    public String getResultPage() {
        return "thankyou";
	}

}
