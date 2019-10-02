// Copyright 2015-2019 SWIM.AI inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
package swim.iris.agents;

import com.opencsv.CSVReader;
import com.opencsv.bean.CsvToBeanBuilder;
import swim.api.SwimLane;
import swim.api.lane.ValueLane;
import swim.iris.beans.TrainingRecord;

import java.util.Iterator;

public class TrainingDataAgent extends AbstractDataAgent<TrainingRecord> {
  
  private final static String TRAINING_FILES_PATH = "../data/train/iris_train_%s.csv";
  private final static Integer INITIAL_DELAY = 60 * 1000;
  private final static Integer MIN_DELAY = 5 * 1000;
  private final static Integer MAX_DELAY = 60 * 1000;
  
  @SwimLane ("data")
  private ValueLane<TrainingRecord> data = this.<TrainingRecord>valueLane().didSet((newValue, oldValue) -> {
    System.out.println(nodeUri());
    System.out.println(newValue);
  });
  
  @Override
  public void didStart() {
    
    createDataIterator(TRAINING_FILES_PATH, this.getProp("id").stringValue());
    createTimer(INITIAL_DELAY, MIN_DELAY, MAX_DELAY);
  }
  
  @Override
  Iterator<TrainingRecord> getIterator(CSVReader reader) {
    return new CsvToBeanBuilder<TrainingRecord>(reader).withType(TrainingRecord.class).build().iterator();
  }
  
  @Override
  void setData(TrainingRecord record) {
    this.data.set(record);
  }
}

