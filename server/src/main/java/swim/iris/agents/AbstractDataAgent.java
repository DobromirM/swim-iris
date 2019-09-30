package swim.iris.agents;

import com.opencsv.CSVReader;
import swim.api.agent.AbstractAgent;
import swim.concurrent.TimerRef;

import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.Random;

abstract class AbstractDataAgent<T> extends AbstractAgent {
  
  private Iterator<T> dataIterator;
  private TimerRef timer;
  
  abstract Iterator<T> getIterator(CSVReader reader);
  abstract void setData(T record);
  
  void createTimer(Integer initialDelay, Integer minDelay, Integer maxDelay) {
    this.timer = setTimer(initialDelay, () -> {
      
      readNewRow();
      this.timer.reschedule(getRandomDelay(minDelay, maxDelay));
    });
  }
  
  void createDataIterator(String filePath, String fileSuffix) {
    
    String file = String.format(filePath, fileSuffix);
    
    try {
      CSVReader reader = new CSVReader(new FileReader(file));
      dataIterator = getIterator(reader);
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }
  
  private void readNewRow() {
    
    if (dataIterator.hasNext()) {
      setData(dataIterator.next());
    }
    else {
      this.timer.cancel();
    }
  }
  
  private Integer getRandomDelay(Integer min, Integer max) {
    Random randomGenerator = new Random();
    return randomGenerator.nextInt(max - min) + min;
  }
}
