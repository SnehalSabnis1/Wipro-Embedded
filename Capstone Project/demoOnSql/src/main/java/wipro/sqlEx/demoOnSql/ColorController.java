package wipro.sqlEx.demoOnSql;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ColorController {
	
	@GetMapping("/color")
    public String getColorPage() {
        return "color";
    }

}