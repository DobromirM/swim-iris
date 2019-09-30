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
package swim.iris;

import swim.api.SwimRoute;
import swim.api.agent.AgentRoute;
import swim.fabric.Fabric;
import swim.iris.agents.TestingDataAgent;
import swim.iris.agents.TrainingDataAgent;
import swim.kernel.Kernel;
import swim.api.plane.AbstractPlane;
import swim.server.ServerLoader;
import swim.structure.Value;

public class IrisPlane extends AbstractPlane {
  
  @SwimRoute ("/training/:id")
  AgentRoute<TrainingDataAgent> trainingAgentType;
  
  @SwimRoute ("/testing/:id")
  AgentRoute<TestingDataAgent> testingAgentType;
  
  public static void main(String[] args) {
    final Kernel kernel = ServerLoader.loadServer();
    final Fabric fabric = (Fabric) kernel.getSpace("basic");
    
    kernel.start();
    System.out.println("Running Basic server...");
    kernel.run();
    
    fabric.command("/training/1", "wakeup", Value.absent());
    fabric.command("/training/2", "wakeup", Value.absent());
    fabric.command("/training/3", "wakeup", Value.absent());
    fabric.command("/training/4", "wakeup", Value.absent());

    fabric.command("/testing/1", "wakeup", Value.absent());
    fabric.command("/testing/2", "wakeup", Value.absent());
  }
}
